
"""
Case study example
===================
Here is the sample code for the case study in RecBole, i.e. getting the top-k recommendation results for each user.
"""

from recbole.utils.case_study import full_sort_topk, full_sort_scores
from recbole.quick_start import load_data_and_model
import pandas as pd
import json

OUTPUT_DIR = "/Volumes/Forster Neu/Masterarbeit Data/yelp_dataset/recommendations/recbole/"


model_file = "SimpleX-Jul-11-2024_09-52-56.pth"



# Read user IDs from CSV
df = pd.read_csv("dataset/yelp_sample/yelp_sample.inter", sep="\t")
user_ids = list(set(df["user_id:token"].values.tolist()))


# Load model and data
config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
    model_file=f"saved/{model_file}",
)


print("TEST DATA")
print(test_data.uid2positive_item)


error_count = 0
recommendations = {}

for uid in user_ids: 
    try:

        # Convert external user ID to internal ID
        uid_series = dataset.token2id(dataset.uid_field, [uid])

        # Compute top-k recommendations
        topk_score, topk_iid_list = full_sort_topk(
            uid_series, model, test_data, k=50, device=config["device"]
        )

        #print(f"TOP K SCORES for {uid} :")
        #print(topk_score)  # scores of top 10 items
        #print(topk_iid_list)  # internal id of top 10 items
        # Convert internal item IDs to external tokens
        external_item_list = dataset.id2token(dataset.iid_field, topk_iid_list.cpu())

        # Print or store recommendations
        #print(f"EXTERNAL TOKENS OF TOP k ITEMS FOR USER {uid} :")
        #print(external_item_list)

        # Computing the full scores
        # score = full_sort_scores(uid_series, model, test_data, device=config["device"])
        # print("Score of all items")
        # print(score)


        # print(
        #     score[0, dataset.token2id(dataset.iid_field, ["242", "302"])]
        # )  # score of item ['242', '302'] for user '196'.


        # Store recommendations in the desired format
        recommendations[uid] = [
            {"item_id": item_id, "score": score}
            for item_id, score in zip(external_item_list.tolist(), topk_score.cpu().tolist())
        ]

    except Exception as e:
        print(f"Error for user {uid}: {e}")
        error_count += 1
        continue

# Print error rate
print(f"The error count was {error_count}, which is {error_count/len(user_ids)*100:.2f}% of the total users.")

# Save the recommendations to a JSON file
with open(f"{OUTPUT_DIR}{model_file}.json", "w") as f:
    json.dump(recommendations, f, indent=4)

        
    



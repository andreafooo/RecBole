from recbole.quick_start import run_recbole
import json
from time import time

def run_configurations(model):
    # Run the RecBole model with specified configurations
    output_dict = run_recbole(model=model, config_file_list=["config_test.yaml"])
    
    # Generate the output file path
    # output_directory = f"output/{dataset}_{model}_{epochs}ep_{batch_size}bs_{lr}lr_{int(time())}.json"
    
    # Save the result to a JSON file
    # with open(output_directory, 'w') as f:
    #     json.dump(output_dict, f)
    
    # print(f"Results saved to {output_directory}")

# Example of running the configuration
run_configurations("SimpleX")


# from recbole.quick_start import run_recbole
# import json
# from time import time
# from recbole.config import Config



# # See evaluation metrics: https://recbole.io/docs/recbole/recbole.evaluator.metrics.html

# def run_configurations(model, dataset, epochs, batch_size, lr):

#     # config_dict={'metrics' : ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'GiniIndex','TailPercentage'], 
#     #              'learning_rate': lr, 
#     #              'batch_size': batch_size, 
#     #              'epochs': epochs,
#     #              'TIME_FIELD': 'timestamp:float'}
#     #             #  'eval_args' : {'split' : {'RS': [0.65, 0.15, 0.2]}, 'order' : 'TO', 'group_by': 'user'}
#     #             #  }



#     output_dict = run_recbole(model=model, dataset=dataset, 
#                               config_file_list=["test.yaml"])
#     output_directory = f"output/{dataset}_{model}_{epochs}ep_{batch_size}bs_{lr}lr_{time()}.json"

#     # Save the result to a JSON file
#     with open(output_directory, 'w') as f:
#         json.dump(output_dict, f)

    

# # run_configurations("SimpleX", "gowalla-merged", "output/gowalla_merged_simplex.json", 1)
# #run_configurations("PDA", "gowalla-merged", "output/gowalla_merged_debiased.json", 1)

# # run_configurations("SimpleX", "gowalla-not-merged", "output/gowalla_not_merged_simplex.json", 1)
# # run_configurations("MACR", "gowalla-not-merged", "output/gowalla_not_merged_debiased.json", 1)

# #run_configurations("SimpleX", "yelp", "output/yelp_simplex.json", 1)
# # run_configurations("MACR", "yelp", "output/yelp_debiased.json", 1)


# #run_configurations("SimpleX", "yelp_sample", 20, 1024/4, 0.001)
# #run_configurations("SimpleX", "brightkite_sample", 20, 1024/4, 0.001)
# # run_configurations("SimpleX", "yelp_sample", 20, 1024/2, 0.0025)
# # run_configurations("ItemKNN", "yelp_sample", 20, 1024/2, 0.001)


# run_configurations("ItemKNN","yelp_sample", 20, 1024/2, 0.001)
# # run_configurations("SimpleX","foursquarenyc_sample", 20, 1024/2, 0.001)

# # run_configurations("ItemKNN","foursquaretky_sample", 20, 1024/2, 0.001)
# # run_configurations("SimpleX","foursquaretky_sample", 20, 1024/2, 0.001)

# # run_configurations("ItemKNN", "yelp_sample", 20, 1024/2, 0.001)
# # run_configurations("ItemKNN", "gowalla_sample", 20, 1024/2, 0.001)
# # run_configurations("ItemKNN", "brightkite_sample", 20, 1024/2, 0.001)


# # run_configurations("SimpleX", "gowalla_sample", 20, 1024/4, 0.001)
# # run_configurations("ItemKNN", "gowalla_sample", 20, 1024/2, 0.001)

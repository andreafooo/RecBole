cfg_str = """
data_path: dataset/brightkite_sample
dataset: brightkite_sample
field_separator: "\\t"
USER_ID_FIELD: user_id:token
ITEM_ID_FIELD: item_id:token
RATING_FIELD: ~
TIME_FIELD: timestamp:float
show_progress: false

load_col:
    inter: [user_id:token, article_id:token, timestamp:float]
    user: [user_id:token]
    item: [item_id:token]

epochs: 5
learning_rate: 0.01
batch_size: 256
user_inter_num_interval: "[0,inf)"
item_inter_num_interval: "[0,inf)"
filter_inter_by_user_or_item: false
neg_sampling:
    uniform: 1
eval_args:
    split: {'RS': [0.65, 0.15, 0.2]}
    group_by: user_id:token
    order: TO
metrics: ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'MAP', 'GiniIndex', 'TailPercentage']
topk: 12
valid_metric: MAP@
"""


with open("config_test.yaml", "w") as f:
    f.write(cfg_str)

#     field_types:
#   review_id: 'token'
#   user_id: 'token'
#   item_id: 'token'
#   useful: 'float'
#   funny: 'float'
#   cool: 'float'
#   timestamp: 'float'
#   rating: 'float'

# dataset:
#   field_separator: "\t"
#   USER_ID_FIELD: 'user_id:token'
#   ITEM_ID_FIELD: 'item_id:token'
#   TIME_FIELD: 'timestamp:float'
#   LABEL_FIELD: 'rating:float'


# metrics: ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'GiniIndex', 'TailPercentage']
# learning_rate: 0.001
# batch_size: 256
# epochs: 20
# eval_args:
#   split:
#     RS: [0.65, 0.15, 0.2]
#   order: 'TO'
#   group_by: 'user_id:token'

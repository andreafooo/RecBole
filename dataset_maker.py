# https://github.com/RUCAIBox/RecSysDatasets/blob/master/conversion_tools/src/base_dataset.py
import tqdm
import pandas as pd
import os
import numpy as np
import datetime
class BaseDataset(object):
    def __init__(self, input_path, output_path):
        super(BaseDataset, self).__init__()

        self.dataset_name = ''
        self.input_path = input_path
        self.output_path = output_path
        self.check_output_path()

        # input file
        self.inter_file = os.path.join(self.input_path, 'inters.dat')
        self.item_file = os.path.join(self.input_path, 'items.dat')
        self.user_file = os.path.join(self.input_path, 'users.dat')
        self.sep = '\t'

        # output file
        self.output_inter_file, self.output_item_file, self.output_user_file = self.get_output_files()

        # selected feature fields
        self.inter_fields = {}
        self.item_fields = {}
        self.user_fields = {}

    def check_output_path(self):
        if not os.path.isdir(self.output_path):
            os.makedirs(self.output_path)

    def get_output_files(self):
        output_inter_file = os.path.join(self.output_path, self.dataset_name + '.inter')
        output_item_file = os.path.join(self.output_path, self.dataset_name + '.item')
        output_user_file = os.path.join(self.output_path, self.dataset_name + '.user')
        return output_inter_file, output_item_file, output_user_file

    def load_inter_data(self) :
        raise NotImplementedError

    def load_item_data(self):
        raise NotImplementedError

    def load_user_data(self):
        raise NotImplementedError

    def convert_inter(self):
        try:
            input_inter_data = self.load_inter_data()
            self.convert(input_inter_data, self.inter_fields, self.output_inter_file)
        except NotImplementedError:
            print('This dataset can\'t be converted to inter file\n')

    def convert_item(self):
        try:
            input_item_data = self.load_item_data()
            self.convert(input_item_data, self.item_fields, self.output_item_file)
        except NotImplementedError:
            print('This dataset can\'t be converted to item file\n')

    def convert_user(self):
        try:
            input_user_data = self.load_user_data()
            self.convert(input_user_data, self.user_fields, self.output_user_file)
        except NotImplementedError:
            print('This dataset can\'t be converted to user file\n')

    @staticmethod
    def convert(input_data, selected_fields, output_file):
        output_data = pd.DataFrame()
        for column in selected_fields:
            output_data[column] = input_data.iloc[:, column]
        with open(output_file, 'w') as fp:
            fp.write('\t'.join([selected_fields[column] for column in output_data.columns]) + '\n')
            for i in tqdm(range(output_data.shape[0])):
                fp.write('\t'.join([str(output_data.iloc[i, j])
                                    for j in range(output_data.shape[1])]) + '\n')

    def parse_json(self, data_path):
        with open(data_path, 'rb') as g:
            for l in g:
                yield eval(l)

    def getDF(self, data_path):
        i = 0
        df = {}
        for d in self.parse_json(data_path):
            df[i] = d
            i += 1
        data = pd.DataFrame.from_dict(df, orient='index')
        
        return data
    


class BrightkiteDataset(BaseDataset):
    def __init__(self, input_path, output_path):
        super(BrightkiteDataset, self).__init__(input_path, output_path)
        self.dataset_name = "brightkite_sample"

        self.inter_file = os.path.join(self.input_path, "brightkite_sample.inter")
        self.item_file = os.path.join(self.input_path, "brightkite_sample.item")
        self.user_file = os.path.join(self.input_path, "brightkite_sample.user")

        self.sep = ","

        # output_path
        output_files = self.get_output_files()
        self.output_inter_file = output_files[0]
        self.output_item_file = output_files[1]
        self.output_user_file = output_files[2]

        # selected feature fields
        self.inter_fields = {
            0: "review_id:token",
            1: "item_id:token",
            2: "timestamp:float",
            3: "rating:float",
            
        }

        self.item_fields = {
            0: "business_id:token	latitude:float	longitude:float"
        }

        self.user_fields = {
            0: "customer_id:token",
        }

    def load_inter_data(self):
        df = pd.read_csv(self.inter_file,
            dtype={"t_dat": "object", "customer_id": "object", "article_id": "object", "price": float, "sales_channel_id": int}
           )
        # approx. 1 month + 2 weeks
        df = df[-len(df)*3//48:].reset_index(drop=True)
        # Further downsampling to avoid OOM
        uus = df["customer_id"].unique()
        sampled_users = np.random.choice(uus, len(uus)//6)
        df = df.query('customer_id in @sampled_users')
        df['t_dat'] = df['t_dat'].apply(lambda x: datetime.timestamp(datetime.strptime(x, "%Y-%m-%d")))
        return df

    def load_item_data(self):
        return pd.read_csv(self.item_file, delimiter=self.sep, engine="python")

    def load_user_data(self):
        return pd.read_csv(self.user_file, delimiter=self.sep, engine="python")

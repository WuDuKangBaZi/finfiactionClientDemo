import requests
import traceback

class Mrapx():
    def __init__(self):
        self.host = "http://127.0.0.1:8700"
        self.workflow_list = {}

    def check_status(self) -> dict:
        host_url = self.host + "/robot/state"
        header = {"content-type": "application/json"}
        # 通过get方式发送请求
        try:
            response = requests.get(host_url, headers=header)
            if response.status_code == 200:
                return response.json()['error_code']  # 注意 该项目前意义不明确
        except:
            print(traceback.format_exc())
            return {}

    def list_mrpax(self) -> dict:
        host_url = self.host + "/mrpa/list"
        header = {"content-type": "application/json"}
        # 通过get方式发送请求
        response = requests.get(host_url, headers=header)
        # 获取返回的json数据
        mrap_dict = {}
        if response.status_code == 200:
            json_entity = response.json()
            for entity in json_entity['mrpa_file_list']:
                mrap_dict[entity['file_name'].split(".")[0]] = entity['mrpa_id']
        return mrap_dict  # 获取rpa流程列表

    def execute(self, mrpa_id: str, value: dict) -> str:
        """
        :param mrpa_id:
        :param value:
        :return:
        """
        host_url = self.host + f"/executor/run/async/{mrpa_id}"
        header = {"content-type": "application/json"}
        # 通过post方式发送请求
        try:
            response = requests.post(host_url, headers=header, json=value)
            if response.status_code == 200:
                rep = response.json()
                workflow_id = rep['workflow_id']
                self.workflow_list[workflow_id] = False
                return workflow_id
        except:
            return None

    def check_all_workflow_result(self):
        for workflow_id in self.workflow_list.keys():
            host_url = self.host + f"/executor/result/{workflow_id}"
            header = {"content-type": "application/json"}
            response = requests.post(host_url, headers=header)
            if response.status_code == 200:
                self.workflow_list[workflow_id] = response.json()['result']

    def check_workflow_result(self, workflow_id: str):
        host_url = self.host + f"/executor/result/{workflow_id}"
        header = {"content-type": "application/json"}
        try:
            response = requests.post(host_url, headers=header)
            print("check_workflow_result:", response.json())
            if response.status_code == 200:
                if response.json()['output'] != {}:
                    return response.json()['output']
            return None
        except:
            return None

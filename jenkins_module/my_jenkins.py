# !usr/bin/env/python3 
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : jenkins process
# ************************************************************************
# Imports
# ************************************************************************
from typing import Tuple
import xml.etree.ElementTree as ET
import jenkins
from settings import Config


class MyJenkins():
    def __init__(self) -> None:
        self.props = Config()
        self.server = jenkins.Jenkins(self.props.jenkins_url, username=self.props.user_name, password=self.props.jenkins_apikey)

    def create(self, job_name: str, job_desc: str, git_url: str, git_branch: str,
               teams_url: str, target_folder: str, weekday: Tuple[int], build_time: str) -> bool:
        base_job_config = self.server.get_job_config(self.props.base_job_name)
        result = True

        new_job_config = self._edit(job_name, base_job_config, job_desc, git_url, git_branch,
                                    teams_url, target_folder, weekday, build_time)

        self.server.create_job(job_name, new_job_config)

        return result

    def recreate(self) -> None:
        # T.B.D.
        pass

    def _edit(self, job_name: str, config: str, job_desc: str, git_url: str, git_branch: str,
             teams_url: str, target_folder: str, weekday: Tuple[int], build_time: str) -> str:
        root = ET.fromstring(config)

        # job説明設定
        for elem in root.findall('./description'):
            elem.text = job_desc

        # 1番目がgitのURLで2番目がteamsのURLとなる
        urls = [git_url, teams_url]
        # ビルドパラメータ設定
        defaultvalue_elements = root.findall('.//defaultValue')
        for defaultvalue_element, url in zip(defaultvalue_elements, urls):
            defaultvalue_element.text = url

        # ビルド日時設定
        weekday_jenkins = self._conversion_time(weekday, build_time)
        spec_elements = root.findall('.//spec')
        for spec_element in spec_elements:
            spec_element.text = weekday_jenkins

        # Git URL設定
        url_elements = root.findall('.//url')
        for url_element in url_elements:
            url_element.text = git_url

        # Git対象ブランチ設定
        # 複数あった場合の判定
        if '' in git_branch:
            git_branchs = git_branch.replace('', '¥n')
        else:
            git_branchs = git_branch
        name_elements = root.findall('.//name')
        for name_element, i in enumerate(name_elements):
            # nameエレメントは3つあり、その3番目が対象
            if i == 3:
                name_element.text = git_branchs

        # 対象フォルダ設定
        included_regions_elements = root.findall('.//includedRegions')
        for included_regions_element in included_regions_elements:
            included_regions_element.text = target_folder

        # スクリプトパス設定
        scriptpath_elements = root.findall('.//scriptPath')
        for scriptpath_element in scriptpath_elements:
            scriptpath_element.text = './design/' + job_name + '/' + 'jenkins/main.groovy'

        return ET.tostring(root, encoding='utf-8').decode('utf-8')

    def _conversion_time(self, weekday: Tuple[int], build_time: str) -> str:
        build_time_split = build_time.split(":")
        hour = build_time_split[0]
        # 0分の場合はHのハッシュを使用する(Jenkins的にはHが推奨らしいので)
        minute = 'H' if build_time_split[1] == "0" else build_time_split[1]
        time = minute + ' ' + hour + ' '  + '*' + ' ' + '*' + ' '

        active_days = []
        start_day = None
        end_day = None

        for i, day in enumerate(weekday):
            if day == 1:
                if start_day is None:
                    start_day = i
                end_day = i
            elif start_day is not None:
                if start_day == end_day:
                    active_days.append(str(start_day))
                else:
                    active_days.append(f"{start_day}-{end_day}")
                start_day = None
                end_day = None

        if start_day is not None:
            if start_day == end_day:
                active_days.append(str(start_day))
            else:
                active_days.append(f"{start_day}-{end_day}")

        return time + ','.join(active_days)

    def get_all_job(self):
        #return self.server.get_jobs()
        pass

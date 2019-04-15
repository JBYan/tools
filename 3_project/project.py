# This is a script for set up a Customized python engineering
import os
import time
import click
import shutil


@click.command()
@click.option('--type', default=1, help='Type of project.')
@click.option('--project', prompt='Your project name', help='The project name you want to build.')
@click.option('--author', prompt='Your name', help='The author of the project.')
@click.option('--email', prompt='Your email address', help='The email address of the author.')
def main(type, project, author, email):
    """parse parameters from command line."""
    while os.path.exists(project):
        click.echo('The project has been exists. Would you want to rebuild the project?\n')
        click.echo('> {:<12}\tfor\tcontinue'.format('YES'))
        click.echo('> {:<12}\tfor\tbreak'.format('NO'))
        click.echo('> {:<12}\tfor\tbuilding another project\n'.format('PROJECT NAME'))
        confirm_info = input('> ').strip().lower()
        if confirm_info == 'yes':
            shutil.rmtree(project)
        elif confirm_info == 'no':
            return
        else:
            project = confirm_info
    my_project = CreateNewProject(type, project, author, email)
    my_project.run()


class CreateNewProject:
    """
    @NAME:
        创建一个新的工程
    @SYNOPSIS:
        python project.py -[TYPE] PROJECT AUTHOR
    @DESCRIPTION:
        -1 数据分析工程
        -p python2 环境（未实现）
        -P python3 环境（未实现）
    """

    def __init__(self, type, project, author, email):
        self.type = type
        self.project = project
        self.author = author
        self.email = email
        self.project_path = "{}/{}/".format(os.getcwd(), project)

    def create_data_analysis_project(self):
        """
        创建数据分析工程目录
        """
        _format = lambda x: x.format(self.project)

        paths = [
            r"./{}/bin/",
            r"./{}/data/base_data/",
            r"./{}/data/res_data/",
            r"./{}/data/reference/",
            r"./{}/lib/"]
        for path in paths:
            os.makedirs(_format(path))

        files = [
            r"./{}/bin/load_data.py",
            r"./{}/bin/main.py",
            r"./{}/lib/__init__.py",
            r"./{}/lib/util.py",
            r"./{}/lib/config.py"]
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        project_info = [
            "# encoding: utf-8\n",
            '"""\n'
            "@author: {}\n".format(self.author),
            "@contact: {}\n".format(self.email),
            "@time: {}\n".format(local_time),
            '"""']
        for file in files:
            with open(_format(file), 'w', encoding='utf-8') as f:
                f.writelines(project_info)

        return True

    def show_project(self, path, depth=0):
        """
        打印工程信息。
        """
        space = " " * depth * 4
        files = os.listdir(path)
        file_num = len(files)
        for temp_num, _file in enumerate(files):
            file_name = path + "/" + _file
            if (temp_num + 1 < file_num):
                print(space + "├─" + _file + "\n")
            else:
                print(space + "└─" + _file + "\n")
            if os.path.isdir(file_name):
                self.show_project(file_name, depth=depth+1)

    def run(self):
        build_flag = False
        if self.type == 1:
            build_flag = self.create_data_analysis_project()
        if build_flag:
            print("成功生成工程\n\n{}".format(self.project))
            self.show_project(self.project_path)


if __name__ == "__main__":
    main()

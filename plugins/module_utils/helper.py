import re

class Helper(object):
    """
        Helper

        This is a helper utility class
    """  
    def __init__(self) -> None:
        return
    
    def parse_installer_output(output):
        """
        Parse tokens from the output of openshift installer cli create cluster command 
        :output: Stdout string

        :return: Any
        """

        if output is None:
            return None
        
        result = dict(
            api_server_url=dict(type=str, required=True),
            web_console_url=dict(type=str, required=True),
            set_kubeconfig_cmd=dict(type=str, required=True),
            user=dict(type=str, required=True),
            password=dict(type=str, required=True)
        )

        # Regex patterns to extract
        api_url_pattern = re.compile(r'Kubernetes API at (https://\S+)', re.IGNORECASE)
        console_url_pattern = re.compile(r'OpenShift web-console here: (https://\S+)', re.IGNORECASE)
        set_kubeconfig_cmd_pattern = re.compile(r'run \'(export KUBECONFIG=\S+)\'', re.IGNORECASE)
        credentials_pattern=re.compile(r'user: "(.*)", and passwprd: "(.*)"', re.IGNORECASE)

        api_url = re.search(api_url_pattern, output)
        console_url = re.search(console_url_pattern, output)
        set_kubeconfig_cmd = re.search(set_kubeconfig_cmd_pattern, output)
        credentials = re.search(credentials_pattern, output)

        result['api_server_url'] = api_url.group(1) if api_url else None
        result['web_console_url'] = console_url.group(1) if console_url else None
        result['set_kubeconfig_cmd'] = set_kubeconfig_cmd.group(1) if set_kubeconfig_cmd else None
        result['user'] = credentials.group(1) if credentials else None
        result['password'] = credentials.group(2) if credentials else None
        
        return result
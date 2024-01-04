import dataclasses
import subprocess
import re


@dataclasses.dataclass
class Wifi:
    name: str
    security_key: bool | None
    password: str | None


class CMD:
    command = "netsh wlan show profile"

    def _show_all_profiles(self) -> str:
        command = f"{self.command}s".split()
        return subprocess.run(command, capture_output=True).stdout.decode()

    def profiles_names(self) -> list[Wifi]:
        output = self._show_all_profiles()
        names = re.findall("All User Profile {5}: (.*)\r", output)
        return [Wifi(name, security_key=None, password='') for name in names]

    def wifi_password_output(self, wifiobject: Wifi) -> str:
        command = self.command.split()
        if wifiobject.name is not None and wifiobject.security_key is True:
            command.append(wifiobject.name)
            command.append("key=clear")

        return subprocess.run(command, capture_output=True).stdout.decode()

    @staticmethod
    def if_security_key_not_absent(output):
        if re.search('Security key {11}: Absent', output):
            return True
        return False


def main():
    cmd = CMD()

    wlan_list = cmd.profiles_names()

    if len(wlan_list) != 0:
        for wifi in wlan_list:
            wifi_info_output = cmd.wifi_password_output(wifi)
            if cmd.if_security_key_not_absent(wifi_info_output):
                wifi.security_key = False
            else:
                wifi.security_key = True

        for num, wifi in enumerate(wlan_list):
            try:
                wifi_info_output = cmd.wifi_password_output(wifi)
                password = re.search('Key Content {12}: (.*)\r', wifi_info_output)
                wifi.password = password[1]
            except TypeError:
                print(f'wifi {num}: The password was not readable. It will be empty.')
                wifi.password = ''

    [print(num, wlan.name, wlan.password) for num, wlan in enumerate(wlan_list)]


if __name__ == '__main__':
    main()

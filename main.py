from typing import Generator, Any

from requests import get

from converter import to_json, to_xml, to_excel, to_csv


def get_notebooks() -> Generator[dict[str, Any], None, None]:
    """
    Возвращает генератор, который генерирует
    словари с данными об игровых ноутбуках из запросов.
    """
    total_number = 0
    for offset in range(0, total_number + 37, 36):
        cookies = {
            'PHPSESSID': 'sm489kb5kgssqior3gq88ngcu7',
            '_ym_uid': '1641548299951357740',
            '_ym_d': '1650469539',
            'ab_user': '7455922250100',
            'ab_segment': '74',
            'dt': '1',
            'ek_ab_test': 'B',
            'AUTORIZZ': '0',
            'AC': '1',
            'lv_user_org': '0',
            'el_group_user_org': '0',
            'bonus_cobrand_showed': '0',
            'ABT_test': 'C',
            '_dyid_server': '-1837467744367943967',
            '_dyjsession': 'cd69rdeko38aii64jsfblgqclvvs3wrb',
            'dy_fs_page': 'www.eldorado.ru%2F%3Futm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_campaign%3Dgoogle%26utm_referrer%3Dgoogle',
            '_dy_c_exps': '',
            'rcuid': '61b081542403d3000195231a',
            '_gcl_au': '1.1.1585871322.1656086249',
            'utm_campaign': 'google',
            '_dycnst': 'dg',
            '_dy_c_att_exps': '',
            'tmr_lvidTS': '1656086253672',
            'tmr_lvid': '72b6b93e421f71230c954849e4bc6157',
            'advcake_session_id': '5d57dbc0-8826-aebf-2ddb-56b90694fc15',
            'clickcake_id': 'ab43cc73-d640-ff68-0402-277d3f6ee6b0',
            '_userGUID': '0:l4smzx4a:cOuMPrG41D5ubXXxaDPg0S3cLY4smCiC',
            '_dyid': '-1837467744367943967',
            'flocktory-uuid': 'f0dd636f-7da4-4f3b-859f-e36eca7f3210-6',
            'uxs_uid': '655e1be0-f3d6-11ec-b289-c9e77f2da955',
            'USER_AUTH_GTM': '0',
            'bCNT': '0%3A0',
            'BITRIX_SM_ELD_TZ_OFFSET': '-180',
            '_dyfs': '1656086316470',
            'gdeslon.ru.__arc_domain': 'gdeslon.ru',
            'gdeslon.ru.user_id': 'afd637f6-a7e2-450c-aeae-c4fed3a6f7d6',
            'adrcid': 'AePZWW1ecQC9_f_VcUKUyjg',
            'advcake_utm_webmaster': '',
            'advcake_click_id': '',
            'digi-SearchVisitor': '10%3A10',
            'flixgvid': 'flixf1a52334000000.69829374',
            'unauthorizedId': 'uewph1efgm2js4ck8fxizte8h18jp66pfwzad0f899tj4dhnyq1rs9tcym1c7t4ownbn3ifrdjrlarog9v8pv51fzdhi6re2mowcgjzrbbyw5zc51ha8fnnpjaxuhjlprw9k89qc3qvmyqm9ruwvfj2183osa975xgjndahx2esxdjc2kinwsgq93cnsq8rcjk67jhp8a8459q3zboc6cvywzaekus720r6ag67oox7qlho5133tyuv26pvb4okt',
            'last_source': 'www.google.com',
            'advcake_utm_partner': '',
            'advcake_trackid': 'dafb1ae3-e5a9-337e-18ac-a7f48f15aecb',
            'advcake_track_url': 'https%3A%2F%2Fwww.eldorado.ru%2Fcat%2Fdetail%2Figrovoy-noutbuk-msi-stealth-15m-a11uek-275ru%2F',
            '__lhash_': '28aa8cc84b1c698593b0a4b45594fb16',
            'show_region_popup': '0',
            'mindboxDeviceUUID': 'b3c71780-e191-4cea-991f-d450faf7518f',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22b3c71780-e191-4cea-991f-d450faf7518f%22%7D',
            'rrpvid': '259203274906219',
            '_gid': 'GA1.2.579565704.1657217221',
            '_ym_isad': '1',
            'iRegionSectionId': '11300',
            'BITRIX_SM_SALE_UID': '31008516040',
            '_dy_csc_ses': 'cd69rdeko38aii64jsfblgqclvvs3wrb',
            '_dy_geo': 'RU.EU.RU_ROS.RU_ROS_Novoshakhtinsk',
            '_dy_df_geo': 'Russia..Novoshakhtinsk',
            '_dyjsession': 'cd69rdeko38aii64jsfblgqclvvs3wrb',
            'clickcake_rsid': 'ea7a9c17-3521-bf44-c9d7-069aa6a363c9',
            'clickcake_sid': 'bab86dae-26c5-7813-d5cd-06bb97e0a501',
            'dSesn': '833141ae-3f01-2331-49f8-3fdbb2f0eca8',
            '_dvs': '0:l5c3pvl3:QnCuzxON49alxHnmpoz86UZhRo0qo663',
            '_dycst': 'dk.w.c.ms.',
            '_dy_toffset': '-2',
            '__js_p_': '254,900,0,1,0',
            '__jhash_': '192',
            '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.0.0%20Safari%2F537.36',
            '__hash_': '6bbdcdf22449472dfd60712a334d435a',
            'clickcake_total': '63',
            'clickcake_current': '59',
            'clickcake_max': '59',
            'clickcake_clicks_history': '%7B%2220220624%22%3A5%2C%2220220626%22%3A38%2C%2220220627%22%3A5%2C%2220220707%22%3A6%2C%2220220708%22%3A9%7D',
            'clickcake_sessions_history': '%7B%2220220624%22%3A3%2C%2220220626%22%3A10%2C%2220220627%22%3A9%2C%2220220707%22%3A3%2C%2220220708%22%3A5%7D',
            'clickcake_sessions_depth': '%7B%22ea7a9c17-3521-bf44-c9d7-069aa6a363c9%22%3A5%7D',
            'tmr_detect': '1%7C1657264262942',
            '_ga': 'GA1.2.687257966.1656086254',
            '_dy_soct': '1009413.1015420.1656086245.cd69rdeko38aii64jsfblgqclvvs3wrb*1091396.1267618.1656086293.cd69rdeko38aii64jsfblgqclvvs3wrb*1009413.1015421.1656089592.cd69rdeko38aii64jsfblgqclvvs3wrb*1020255.1036211.1656089605.cd69rdeko38aii64jsfblgqclvvs3wrb*1020255.1036209.1656195164.cd69rdeko38aii64jsfblgqclvvs3wrb*1052902.1130398.1656274548.cd69rdeko38aii64jsfblgqclvvs3wrb*1052902.1130394.1656278330.cd69rdeko38aii64jsfblgqclvvs3wrb*1024759.1045344.1657264260*1029321.1119670.1657264260*1062106.1161327.1657264260*1066273.1175622.1657264260*1070188.1311680.1657264260*1070841.1192040.1657264260*1102865.1306896.1657264260*1003181.1004426.1657264260*1047863.1186619.1657264261*1048763.1117338.1657264261*1048769.1117349.1657264261*1028959.1056007.1657264261*1103726.1309862.1657264261*1104304.1311769.1657264261*1024438.1090852.1657264263*1041165.1093589.1657264263',
            '__zzatgib-w-eldorado': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VseGklaAoTJH4UGERmUlBBbloYDxMhdHQ6ehs3V10cESRYDiE/C2lbVjRnFRtASBgvS255LkJnI2NHXCRJXVB1F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NEhY=Ox3hmg==',
            'cfidsgib-w-eldorado': 'OOh+r60H/nK1iAU6+SpknNQfSFNmWkfe6aGVMGw9XcRRHRk7JeiEQcv6Pmol4gIIZy/ClX73/tb6CwmUXjNp2gHi7Kpjg5wEh4D0SesIHNQu7CkofTvih739+PzhbQKNb3VG6vtHL9JNrZazUNBv/JpWqiNi1ae0pToR/z8P',
            'cfidsgib-w-eldorado': 'OOh+r60H/nK1iAU6+SpknNQfSFNmWkfe6aGVMGw9XcRRHRk7JeiEQcv6Pmol4gIIZy/ClX73/tb6CwmUXjNp2gHi7Kpjg5wEh4D0SesIHNQu7CkofTvih739+PzhbQKNb3VG6vtHL9JNrZazUNBv/JpWqiNi1ae0pToR/z8P',
            'gsscgib-w-eldorado': 'aSWa3c47JkWFhoA04xw/5QlCcrJTPIqzbbvg4DxrulwBcLCMUZwGZ140ILMYeKMrZx+zUk7NG5rZ3OJ4J3pdeBJbvtvJi/Y6yM9mlOV3E28Nh9g/EWKqrgWgk1XP07O/qNrKOPJoE92+57wzRyVidcduUyAi19oouGBwRBZd8RGjFo1CJAZCrwxkB5AMpbqmAie1Oyv1nkBCSJYwAL1U5Aa4BTco2dGMi4E6ul+Jtw7Fa80MqEha4olC4FDTkA==',
            '_dc_gtm_UA-44012634-4': '1',
            'tmr_reqNum': '885',
            '_ga_4P3TZK55KZ': 'GS1.1.1657263194.16.1.1657264382.0',
        }

        headers = {
            'authority': 'www.eldorado.ru',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'PHPSESSID=sm489kb5kgssqior3gq88ngcu7; _ym_uid=1641548299951357740; _ym_d=1650469539; ab_user=7455922250100; ab_segment=74; dt=1; ek_ab_test=B; AUTORIZZ=0; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; ABT_test=C; _dyid_server=-1837467744367943967; _dyjsession=cd69rdeko38aii64jsfblgqclvvs3wrb; dy_fs_page=www.eldorado.ru%2F%3Futm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_campaign%3Dgoogle%26utm_referrer%3Dgoogle; _dy_c_exps=; rcuid=61b081542403d3000195231a; _gcl_au=1.1.1585871322.1656086249; utm_campaign=google; _dycnst=dg; _dy_c_att_exps=; tmr_lvidTS=1656086253672; tmr_lvid=72b6b93e421f71230c954849e4bc6157; advcake_session_id=5d57dbc0-8826-aebf-2ddb-56b90694fc15; clickcake_id=ab43cc73-d640-ff68-0402-277d3f6ee6b0; _userGUID=0:l4smzx4a:cOuMPrG41D5ubXXxaDPg0S3cLY4smCiC; _dyid=-1837467744367943967; flocktory-uuid=f0dd636f-7da4-4f3b-859f-e36eca7f3210-6; uxs_uid=655e1be0-f3d6-11ec-b289-c9e77f2da955; USER_AUTH_GTM=0; bCNT=0%3A0; BITRIX_SM_ELD_TZ_OFFSET=-180; _dyfs=1656086316470; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=afd637f6-a7e2-450c-aeae-c4fed3a6f7d6; adrcid=AePZWW1ecQC9_f_VcUKUyjg; advcake_utm_webmaster=; advcake_click_id=; digi-SearchVisitor=10%3A10; flixgvid=flixf1a52334000000.69829374; unauthorizedId=uewph1efgm2js4ck8fxizte8h18jp66pfwzad0f899tj4dhnyq1rs9tcym1c7t4ownbn3ifrdjrlarog9v8pv51fzdhi6re2mowcgjzrbbyw5zc51ha8fnnpjaxuhjlprw9k89qc3qvmyqm9ruwvfj2183osa975xgjndahx2esxdjc2kinwsgq93cnsq8rcjk67jhp8a8459q3zboc6cvywzaekus720r6ag67oox7qlho5133tyuv26pvb4okt; last_source=www.google.com; advcake_utm_partner=; advcake_trackid=dafb1ae3-e5a9-337e-18ac-a7f48f15aecb; advcake_track_url=https%3A%2F%2Fwww.eldorado.ru%2Fcat%2Fdetail%2Figrovoy-noutbuk-msi-stealth-15m-a11uek-275ru%2F; __lhash_=28aa8cc84b1c698593b0a4b45594fb16; show_region_popup=0; mindboxDeviceUUID=b3c71780-e191-4cea-991f-d450faf7518f; directCrm-session=%7B%22deviceGuid%22%3A%22b3c71780-e191-4cea-991f-d450faf7518f%22%7D; rrpvid=259203274906219; _gid=GA1.2.579565704.1657217221; _ym_isad=1; iRegionSectionId=11300; BITRIX_SM_SALE_UID=31008516040; _dy_csc_ses=cd69rdeko38aii64jsfblgqclvvs3wrb; _dy_geo=RU.EU.RU_ROS.RU_ROS_Novoshakhtinsk; _dy_df_geo=Russia..Novoshakhtinsk; _dyjsession=cd69rdeko38aii64jsfblgqclvvs3wrb; clickcake_rsid=ea7a9c17-3521-bf44-c9d7-069aa6a363c9; clickcake_sid=bab86dae-26c5-7813-d5cd-06bb97e0a501; dSesn=833141ae-3f01-2331-49f8-3fdbb2f0eca8; _dvs=0:l5c3pvl3:QnCuzxON49alxHnmpoz86UZhRo0qo663; _dycst=dk.w.c.ms.; _dy_toffset=-2; __js_p_=254,900,0,1,0; __jhash_=192; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.0.0%20Safari%2F537.36; __hash_=6bbdcdf22449472dfd60712a334d435a; clickcake_total=63; clickcake_current=59; clickcake_max=59; clickcake_clicks_history=%7B%2220220624%22%3A5%2C%2220220626%22%3A38%2C%2220220627%22%3A5%2C%2220220707%22%3A6%2C%2220220708%22%3A9%7D; clickcake_sessions_history=%7B%2220220624%22%3A3%2C%2220220626%22%3A10%2C%2220220627%22%3A9%2C%2220220707%22%3A3%2C%2220220708%22%3A5%7D; clickcake_sessions_depth=%7B%22ea7a9c17-3521-bf44-c9d7-069aa6a363c9%22%3A5%7D; tmr_detect=1%7C1657264262942; _ga=GA1.2.687257966.1656086254; _dy_soct=1009413.1015420.1656086245.cd69rdeko38aii64jsfblgqclvvs3wrb*1091396.1267618.1656086293.cd69rdeko38aii64jsfblgqclvvs3wrb*1009413.1015421.1656089592.cd69rdeko38aii64jsfblgqclvvs3wrb*1020255.1036211.1656089605.cd69rdeko38aii64jsfblgqclvvs3wrb*1020255.1036209.1656195164.cd69rdeko38aii64jsfblgqclvvs3wrb*1052902.1130398.1656274548.cd69rdeko38aii64jsfblgqclvvs3wrb*1052902.1130394.1656278330.cd69rdeko38aii64jsfblgqclvvs3wrb*1024759.1045344.1657264260*1029321.1119670.1657264260*1062106.1161327.1657264260*1066273.1175622.1657264260*1070188.1311680.1657264260*1070841.1192040.1657264260*1102865.1306896.1657264260*1003181.1004426.1657264260*1047863.1186619.1657264261*1048763.1117338.1657264261*1048769.1117349.1657264261*1028959.1056007.1657264261*1103726.1309862.1657264261*1104304.1311769.1657264261*1024438.1090852.1657264263*1041165.1093589.1657264263; __zzatgib-w-eldorado=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VseGklaAoTJH4UGERmUlBBbloYDxMhdHQ6ehs3V10cESRYDiE/C2lbVjRnFRtASBgvS255LkJnI2NHXCRJXVB1F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NEhY=Ox3hmg==; cfidsgib-w-eldorado=OOh+r60H/nK1iAU6+SpknNQfSFNmWkfe6aGVMGw9XcRRHRk7JeiEQcv6Pmol4gIIZy/ClX73/tb6CwmUXjNp2gHi7Kpjg5wEh4D0SesIHNQu7CkofTvih739+PzhbQKNb3VG6vtHL9JNrZazUNBv/JpWqiNi1ae0pToR/z8P; cfidsgib-w-eldorado=OOh+r60H/nK1iAU6+SpknNQfSFNmWkfe6aGVMGw9XcRRHRk7JeiEQcv6Pmol4gIIZy/ClX73/tb6CwmUXjNp2gHi7Kpjg5wEh4D0SesIHNQu7CkofTvih739+PzhbQKNb3VG6vtHL9JNrZazUNBv/JpWqiNi1ae0pToR/z8P; gsscgib-w-eldorado=aSWa3c47JkWFhoA04xw/5QlCcrJTPIqzbbvg4DxrulwBcLCMUZwGZ140ILMYeKMrZx+zUk7NG5rZ3OJ4J3pdeBJbvtvJi/Y6yM9mlOV3E28Nh9g/EWKqrgWgk1XP07O/qNrKOPJoE92+57wzRyVidcduUyAi19oouGBwRBZd8RGjFo1CJAZCrwxkB5AMpbqmAie1Oyv1nkBCSJYwAL1U5Aa4BTco2dGMi4E6ul+Jtw7Fa80MqEha4olC4FDTkA==; _dc_gtm_UA-44012634-4=1; tmr_reqNum=885; _ga_4P3TZK55KZ=GS1.1.1657263194.16.1.1657264382.0',
            'pragma': 'no-cache',
            'referer': 'https://www.eldorado.ru/c/noutbuki/f/igrovye/?m=DELIVERY,SELF_DELIVERY,pickupToday',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

        params = {
            'limit': '36',
            'offset': str(offset),
            'orderField': 'popular',
            'orderDirection': 'DESC',
            'smallFacetValues': '[{"code":"pickupToday"},{"code":"DELIVERY"},{"seoURL":"igrovye"},{"code":"SELF_DELIVERY"}]',
            'tags': '[]',
        }

        response = get(
            'https://www.eldorado.ru/sem/v3/A711/categories/noutbuki/products',
            params=params,
            cookies=cookies,
            headers=headers
        ).json()

        total_number = response['totalCount']

        if offset <= total_number:
            print(f'{offset}/{total_number}')
        else:
            print(f'{total_number}/{total_number}')

        for notebook_raw in response['data']:
            yield get_notebook(notebook_raw)
        offset += 36


def get_notebook(notebook_raw: dict[str, Any]) -> dict[str, Any]:
    """
    Возвращает словарь с данными о текущем игровом ноутбуке.
    """
    notebook = dict()
    notebook['Название'] = f"{notebook_raw['brandName']} {notebook_raw['model']}"
    notebook['Цена'] = int(notebook_raw['price'])
    notebook['Старая цена'] = int(notebook_raw['oldPrice'])
    if notebook['Старая цена']:
        notebook['Скидка'] = round(
            100 - (notebook['Цена'] / notebook['Старая цена']) * 100)
    else:
        notebook['Скидка'] = 0
    notebook['Бонусы за покупку'] = round(notebook['Цена'] * 0.03)
    # notebook['Наличие'] = 'В наличии' if notebook_raw['fastOrder'] else 'Нет'
    cpu_raw = notebook_raw['listingDescription'][2]['attributeNameToValueMap']
    notebook['Процессор'] = f"{cpu_raw.get('Производитель процессора', '')} " \
                            f"{cpu_raw.get('Модель процессора', '')} " \
                            f"{cpu_raw.get('Тактовая частота', '')}"
    gpu_raw = notebook_raw['listingDescription'][5]['attributeNameToValueMap']
    notebook['Видеокарта'] = f"{gpu_raw.get('Производитель видеокарты', 'Нет')} " \
                             f"{gpu_raw.get('Модель видеокарты', '')} " \
                             f"{gpu_raw.get('Объем видеопамяти', '')}"
    ram_raw = notebook_raw['listingDescription'][3]['attributeNameToValueMap']
    notebook['Оперативная память'] = f"{ram_raw.get('Объем оперативной памяти', '')} " \
                                     f"{ram_raw.get('Тип оперативной памяти', '')}"
    storage_device_raw = notebook_raw['listingDescription'][4]['attributeNameToValueMap']
    notebook['Накопитель'] = f"{storage_device_raw.get('Объем накопителя', '')} " \
                             f"{storage_device_raw.get('Тип накопителя', '')}"
    screen_raw = notebook_raw['listingDescription'][1]['attributeNameToValueMap']
    notebook['Экран'] = f"{screen_raw.get('Разрешение экрана', '')[:-5]} " \
                        f"{screen_raw.get('Диагональ экрана', '')}"
    notebook[
        'Операционная система'] = f"{notebook_raw['listingDescription'][0]['attributeNameToValueMap'].get('Операционная система', 'Без ОС')}"
    notebook['Ссылка'] = f"https://www.eldorado.ru/cat/detail/{notebook_raw['code']}/"

    for name, value in notebook.items():
        if not value:
            notebook[name] = "Нет"

    return notebook


def main():
    column_names = ['Название',
                    'Цена',
                    'Старая цена',
                    'Скидка',
                    'Бонусы за покупку',
                    'Процессор',
                    'Видеокарта',
                    'Оперативная память',
                    'Накопитель',
                    'Экран',
                    'Операционная система',
                    'Ссылка']

    notebooks = list(get_notebooks())

    to_excel(notebooks, column_names, file_name="notebooks")
    to_json(notebooks, file_name="notebooks")
    to_xml(
        notebooks,
        parameters=column_names,
        root='Ноутбуки',
        item_name='Ноутбук',
        file_name="notebooks"
    )
    to_csv(notebooks, column_names, file_name="notebooks")


if __name__ == '__main__':
    main()

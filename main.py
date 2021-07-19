import pandas as pd
import ipinfo
import socket

access_token = "58f42c5239f3e7"

raw_data = pd.read_csv('data/Schniff.csv')



def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def get_city_for_ip_list(list_of_addresses):
    locations_destination = []
    for ip in list_of_addresses:
        if is_valid_ipv6_address(ip) | is_valid_ipv4_address(ip):
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(ip)
            info = details.all
            if ('city' in info):
                locations_destination.append(info['city'])

    return locations_destination

def get_city_for_ip(ip):

    if is_valid_ipv6_address(ip) | is_valid_ipv4_address(ip):
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(ip)
            info = details.all
            if ('city' in info):
                return info['city']

    return 'nicht feststellbar'

def check_if_df_contains(value, dataframe_colum)->bool:
    return value in dataframe_colum




ip_addresses_des = pd.DataFrame(raw_data.Destination.unique())
ip_addresses_source = pd.DataFrame(raw_data.Source.unique())


unique_destination_df = pd.DataFrame(raw_data.Destination.value_counts())
unique_source_df = pd.DataFrame(raw_data.Source.value_counts())

unique_source_df = unique_source_df.reset_index()
unique_source_df.rename(columns={'index':'Ursprungsadressen', 'Source': 'Vorkommen'}, inplace= True)
unique_source_df['Origin'] = unique_source_df['Ursprungsadressen'].apply(get_city_for_ip)

unique_destination_df = unique_destination_df.reset_index()
unique_destination_df.rename(columns={'index':'Ursprungsadressen', 'Destination': 'Vorkommen'}, inplace= True)
unique_destination_df['Origin'] = unique_destination_df['Ursprungsadressen'].apply(get_city_for_ip)


unique_destination_df.to_csv('data/Destination.csv')
unique_source_df.to_csv('data/Source.csv')
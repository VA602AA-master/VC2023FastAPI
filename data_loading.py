import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_PATH = '/path/to/VAST-Challenge-2023'
PATH_TO_MC1 = f'{BASE_PATH}/MC1/V1/MC1.json'
PATH_TO_MC2 = f'{BASE_PATH}/MC2/mc2_challenge_graph/mc2_challenge_graph.json'
PATH_TO_MC3 = f'{BASE_PATH}/MC3/MC3.json'
PATH_TO_MC_BUNDLES = '/home/sax/Desktop/VAST-Challenge-2023/MC2/bundles'


# Load the json file for Mini Challenge 1 (MC1)
def load_mc1():
    with open(PATH_TO_MC1) as f:
        data = json.load(f)
    return data


# Load the json file for Mini Challenge 2 (MC2)
def load_mc2():
    with open(PATH_TO_MC2) as f:
        data = json.load(f)
    return data


def load_mc3():
    with open(PATH_TO_MC3) as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    data = load_mc1()
    # print keys of the loaded data
    print('keys', data.keys())
    print('is directed', data['directed'])
    print('is multigraph', data['multigraph'])
    print('# nodes', len(data['nodes']))
    print('first node', data['nodes'][0])

    # create a set of all the keys in the nodes
    node_keys = set()
    for node in data['nodes']:
        node_keys.update(node.keys())
    print('node keys', node_keys)

    #export the list of nodes on a csv file with the following columns:
    # id, type, dataset, country
    # leaving blank the fields when missing
    # the content can contain unicode characters, so it is important to use the utf-8 encoding
    with open('mc1_nodes.csv', 'w') as f:
        f.write('id,type,dataset,country\n')
        for node in data['nodes']:
            f.write(f"{node['id']},{node.get('type', '')},{node.get('dataset', '')},{node.get('country', '')}\n")

    # create a set of all the keys in the links
    link_keys = set()
    for link in data['links']:
        link_keys.update(link.keys())
    print('link keys', link_keys)

    #export the list of links on a csv file with the following columns:
    # source, target, type, dataset, weight, key
    # leaving blank the fields when missing
    with open('mc1_links.csv', 'w') as f:
        f.write('source,target,type,dataset,weight,key\n')
        for link in data['links']:
            f.write(
                f"{link['source']},{link['target']},{link.get('type', '')},{link.get('dataset', '')},{link.get('weight', '')},{link.get('key', '')}\n")

    print('# links', len(data['links']))
    print('first link', data['links'][0])
    print('=============================================')

    # print statistics of the MC2 data
    print('Loading MC2 data')
    data2 = load_mc2()
    print('keys', data2.keys())
    print('is directed', data2['directed'])
    print('is multigraph', data2['multigraph'])
    print('# nodes', len(data2['nodes']))
    print('first node', data2['nodes'][0])

    print('# links', len(data2['links']))
    print('first link', data2['links'][0])

    # create a set of all the unique keys in the nodes
    node_keys = set()
    for node in data2['nodes']:
        node_keys.update(node.keys())
    print('node keys', node_keys)
    # create a set of all the unique keys in the links
    link_keys = set()
    for link in data2['links']:
        link_keys.update(link.keys())
    print('link keys', link_keys)

    print('============ Bundle MC2 =====================')
    bundle_names = ['carp', 'catfish', 'chub_mackerel', 'herring', 'mackerel',
                    'salmon', 'shark', 'cod2', 'lichen', 'pollock', 'salmon_wgl', 'tuna']
    for bundle_name in bundle_names:
        print('Loading bundle', bundle_name)
        bundle_file = f'{PATH_TO_MC_BUNDLES}/{bundle_name}.json'
        with open(bundle_file) as f:
            bundle_data = json.load(f)
        # print('bundle keys', bundle_data.keys())
        print('bundle # nodes', len(bundle_data['nodes']))
        print('bundle # links', len(bundle_data['links']))
        # print('first node', bundle_data['nodes'][0])
        # print('first link', bundle_data['links'][0])
        # key set of nodes
        node_keys = set()
        for node in bundle_data['nodes']:
            node_keys.update(node.keys())
        print('node keys', node_keys)
        # key set of links
        link_keys = set()
        for link in bundle_data['links']:
            link_keys.update(link.keys())
        print('link keys', link_keys)
        print('=============================================')

    print('=============================================')
    print('Loading MC3 data')
    data3 = load_mc3()
    print('keys', data3.keys())
    print('is directed', data3['directed'])
    print('is multigraph', data3['multigraph'])
    print('# nodes', len(data3['nodes']))
    print('first node', data3['nodes'][0])

    # create a set of all the keys in the nodes
    node_keys = set()
    for node in data3['nodes']:
        node_keys.update(node.keys())
    print('node keys', node_keys)

    # create a set of all the keys in the links
    link_keys = set()
    for link in data3['links']:
        link_keys.update(link.keys())
    print('link keys', link_keys)

    print('# links', len(data3['links']))
    print('first link', data3['links'][0])
    print('=============================================')
    print('All data loaded successfully')

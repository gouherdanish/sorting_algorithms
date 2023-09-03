from sort_factory import SortFactory
import argparse

if __name__=='__main__':
    arg_parser = argparse.ArgumentParser(description='Sort Algo')
    arg_parser.add_argument('--array', type=str)
    arg_parser.add_argument('--sort', type=str)

    args = arg_parser.parse_args()

    arr = [int(x) for x in args.array.split(' ')]
    sort_engine = SortFactory.get_handler(args.sort)
    sorted_array = sort_engine.sort(arr)
    print(f"sorted_arry - {sorted_array}")

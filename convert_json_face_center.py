"""Writing a Class to perform the whole operation"""
import argparse
import ffmpeg
import pandas as pd
import pprint
import os

#GET PATH
PATH = os.getcwd()
print(PATH)

class JSONIFY:

       

        def jsonify_face(self,csvface) ->dict:
                """returns json from the csv file for the face csv"""
                csv_data = pd.read_csv(csvface)
                print(csv_data)
                json_data = csv_data.to_json(PATH + '\\fileface.json')
                print(json_data)

        def jsonify_centre(self,csvcenter) -> dict:
                """returns json from the csv file for the center csv"""
                csv_data = pd.read_csv(csvcenter)
                print(csv_data)
                json_data = csv_data.to_json(PATH + '\\filecenter.json')
                print(json_data)










if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # provide path to csv files after the command line argument --csvface and --csvcenter
    parser.add_argument('--csvface', type = str ) 
    parser.add_argument('--csvcenter', type = str )

  

    args = parser.parse_args()
    instantiate_jsonify = JSONIFY()
    instantiate_jsonify.jsonify_face(args.csvface)
    instantiate_jsonify.jsonify_centre(args.csvcenter)
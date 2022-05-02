"""Writing a Class to perform the whole operation"""
import argparse
import ffmpeg
import pandas as pd
import pprint
import os
from csv import writer
#GET PATH
PATH = os.getcwd()
print(PATH)

class JSONIFY:

       

        def jsonify_face(self,csvface,csvcenter) ->dict:
                """returns json from the csv file for the face csv"""
                csv_face_data = pd.read_csv(csvface)
                csv_center_data = pd.read_csv(csvcenter)
                print(csv_face_data)
                print("*************______________")
                print(len(csv_face_data)) #start index from here
                # print(len(csv_center_data))
                # print(csv_face_data)
                difference = len(csv_center_data)- len(csv_face_data)
                print(difference)
                # get data to append:
                appendlist = []
                # print(csv_face_data.iloc[len(csv_face_data)-1]['x1'])
                x1 = csv_face_data.iloc[len(csv_face_data)-1]['x1']
                y1 = csv_face_data.iloc[len(csv_face_data)-1]['y1']
                x2 = csv_face_data.iloc[len(csv_face_data)-1]['x2']
                y2 = csv_face_data.iloc[len(csv_face_data)-1]['y2']
                # appendlist.append(x1)
                # appendlist.append(y1)
                # appendlist.append(x2)
                # appendlist.append(y2)
                # csv_face_data = (csv_face_data.drop('frameId',axis = 1))
                # for  i in range(0,difference):
                #         csv_face_data.loc[len(csv_face_data.index)] = appendlist
                # print("______________*************")
                # print(len(csv_face_data))
                # print(csv_face_data)
                
               
                json_data = csv_face_data.to_json(PATH + '\\fileface_recorded.json')
                print(json_data)

        def jsonify_centre(self,csvcenter) -> dict:
                """returns json from the csv file for the center csv"""
                csv_data = pd.read_csv(csvcenter)
              
                csv_data = (csv_data.drop('frameId',axis = 1))
                print(csv_data)
                json_data = csv_data.to_json(PATH + '\\filecenter_recorded.json')
                print(json_data)










if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # provide path to csv files after the command line argument --csvface and --csvcenter
    parser.add_argument('--csvface', type = str ) 
    parser.add_argument('--csvcenter', type = str )

  

    args = parser.parse_args()
    instantiate_jsonify = JSONIFY()
    instantiate_jsonify.jsonify_face(args.csvface,args.csvcenter)
    instantiate_jsonify.jsonify_centre(args.csvcenter)
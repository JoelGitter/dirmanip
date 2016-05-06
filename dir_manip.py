import os, time
import datetime
import shutil
from time import mktime


class DirManip(object):
    '''***********************************************************

        Deleter Class
        Description:  Handle dynamic file manipulation needs
        Date Created:  04/27/2016
        Notes:

    ***********************************************************'''
    def __init__(self, from_path, days_back, delete_move, to_path = ''):
        self.from_path = from_path
        self.days_back = days_back
        self.to_path = to_path
        if delete_move == 'DELETE' or delete_move == 'MOVE':
            self.delete_move = delete_move
        else:
            print("Invalid parameter, please enter 'DELETE' or 'MOVE' for the deleteMove variable.")
            return

    def delete_or_move(self):
        #Initialize variables
        root_dir = self.from_path
        to_path = self.to_path
        delete_move = self.delete_move
        time_var = datetime.datetime.now()
        counter = 0
        dirs_count = 0
        deleted_dirs = []

        if delete_move == 'DELETE':
            print('Deleting folders...')
        elif delete_move == 'MOVE':
            print('Moving folders...')

        try:
        
            #Loop through files in directory
            for file in os.walk(root_dir):
                
                #Get the creation date of the file
                dir_creation_date = (datetime.datetime.fromtimestamp(mktime(time.gmtime(os.path.getctime(file[0])))))

                #Get the current date
                current_date = (datetime.datetime.fromtimestamp(mktime(time.localtime())))

                #How many days of data do we want to keep, everything beyond will be deleted
                days = datetime.timedelta(days = self.days_back)
                days_ago = current_date - days

                #Make the gm time the same as local time
                hours = datetime.timedelta(hours = 8)
                dir_creation_date = dir_creation_date - hours
                
                #If the creation date of the folder is beyond date we want to keep, delete the folder
                if dir_creation_date < days_ago:
                    
                    if counter != 0: #Don't delete/move the root directory

                        dirs_count += 1 #Count how many folders are being deleted
                        deleted_dirs.append(file[0]) #List the folders being deleted

                        if delete_move == 'DELETE':
                            shutil.rmtree(file[0]) #Delete the folders
                        elif delete_move == 'MOVE':
                            shutil.move(file[0], to_path) #Move the folders
                            
                counter += 1

            if delete_move == 'DELETE':
                print('{0} folders were deleted...'.format(dirs_count))
            elif delete_move == 'MOVE':
                print('{0} folders were moved...'.format(dirs_count))
                
            #print(deletedDirs) #List of the folders that were deleted

        except:
            pass

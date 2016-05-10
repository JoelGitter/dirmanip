import os, time
import datetime
import shutil
from time import mktime


class DirManip(object):
    '''***********************************************************

        Description:  Handle dynamic file manipulation needs
        Date Created:  04/27/2016
        Notes:

    ***********************************************************'''
    def __init__(self, from_path, to_path = ''):
        self.from_path = from_path
        self.to_path = to_path

    def directory_manipulator(self, keep_days, decision):
        '''Pass in number of days we do not want to touch, the rest will be
        deleted or moved based off of the decision parameter'''

        counter = 0
        dirs_count = 0
        deleted_dirs = []
        self.keep_days = keep_days
        root_dir = self.from_path
        to_path = self.to_path
        time_var = datetime.datetime.now()
        
        if decision.upper() == 'DELETE' or decision.upper() == 'MOVE':
            self.decision = decision
        else:
            print("Invalid parameter, please enter 'DELETE' or 'MOVE' for the deleteMove variable.")
            return

        if self.decision.upper() == 'DELETE':
            print('Deleting folders...')
        elif self.decision.upper() == 'MOVE':
            print('Moving folders...')

        try:
        
            #Loop through files in directory
            for file in os.walk(root_dir):
                '''Loop through and delete/move child directories'''

                #Get the creation date of the file
                dir_creation_date = (datetime.datetime.fromtimestamp(mktime(time.gmtime(os.path.getctime(file[0])))))

                #Get the current date
                current_date = (datetime.datetime.fromtimestamp(mktime(time.localtime())))

                #How many days of data do we want to keep, everything beyond will be deleted
                days = datetime.timedelta(days = self.keep_days)
                days_ago = current_date - days

                #Make the gm time the same as local time
                hours = datetime.timedelta(hours = 8)
                dir_creation_date = dir_creation_date - hours
                
                #If the creation date of the folder is beyond date we want to keep, delete the folder
                if dir_creation_date < days_ago:
                    
                    if counter != 0: #Don't delete/move the root directory
                    
                        dirs_count += 1 #Count how many folders are being deleted/moved
                        deleted_dirs.append(file[0]) #List of the folders being deleted/moved

                        if self.decision.upper() == 'DELETE':
                            shutil.rmtree(file[0]) #Delete the folders
                        elif self.decision.upper() == 'MOVE':
                            shutil.move(file[0], to_path) #Move the folders
                            
                counter += 1

            if self.decision.upper() == 'DELETE':
                print('{0} folders were deleted...'.format(dirs_count))
            elif self.decision.upper() == 'MOVE':
                print('{0} folders were moved...'.format(dirs_count))
                
            #print(deletedDirs) #List of the folders that were deleted

        except:
            raise

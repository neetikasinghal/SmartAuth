import os

import dill as pickle
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import time

class GMMmodel(object):

    def generate_model(self, user, features):
        current_milli_time = lambda: int(round(time.time() * 1000))
        beforetime = current_milli_time()
        dest = "bin/models/"
        dir = "{0}{1}{2}".format(os.path.abspath(os.curdir), "/",dest)
        gmm = GMM(n_components=2, covariance_type='full', n_init=3)
        gmm.fit(features)
        picklefile = "{0}/{1}{2}.gmm".format(os.path.abspath(os.curdir), dest, user)
        with open(picklefile, 'wb') as f:
            pickle.dump(gmm,f)
        # print ('- learning speaker:', picklefile, " with data point = ", features.shape)
        aftertime = current_milli_time()
        print("Time taken to create speaker model: ",aftertime-beforetime," ms")


    def validate_model(self,user,features):
        current_milli_time = lambda: int(round(time.time() * 1000))
        beforetime = current_milli_time()
        modelpath = os.path.abspath(os.curdir) + "/bin/models/"
        gmm_files = [os.path.join(modelpath, fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]
        models = []
        for fname in gmm_files:
            with open(fname, 'rb') as pickle_file:
                models.append(pickle.load(pickle_file))
            speakers = [fname.split("/")[-1].split(".gmm")[0] for fname
                        in gmm_files]

        log_likelihood = np.zeros(len(models))

        for i in range(len(models)):
            gmm = models[i]  # checking with each model one by one
            scores = np.array(gmm.score(features))
            log_likelihood[i] = scores.sum()

        winner = np.argmax(log_likelihood)
        if (speakers[winner]==user):
            print("\nWelcome {} !! Have a good day!".format(user))
            print("\n")
        else:
            print ("\nSorry! We couldn't identify you. Have you registered? If yes, please try authenticating once again")
            print("\n")
        aftertime = current_milli_time()
        print("Time taken to verify speaker : ", aftertime - beforetime," ms")

    def development_model(self,features,models,name):
        gmm = GMM(n_components=2, covariance_type='full',n_init=3)
        gmm.fit(features)
        picklefile = "{0}/{1}/{2}.gmm".format(os.path.abspath(os.curdir), models, name)
        with open(picklefile, 'wb') as f:
           pickle.dump(gmm, f)

        print ('- development modeling completed for :', name, 'with gmm ', picklefile)


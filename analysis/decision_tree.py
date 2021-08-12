from ml import *
from sklearn import tree
# import matplotlib - very important
import matplotlib.pyplot as plt
# import confusion matrix
from sklearn.metrics import confusion_matrix
# import seaborn
import seaborn as sns
from cf_matrix import *
from matplotlib.colors import ListedColormap
import numpy as np
import datetime

def decision_tree(model_name="decision_tree"):
    TARGET_NAME = "result"
    FEATURE_NAMES = ["elo_diff", "time_since_gm_diff", "gm_age_diff"]
    model, ohe, train_df, test_df = get_trained_model("chess", model_name, TARGET_NAME, FEATURE_NAMES)
    test_acc, test_y_pred, test_y_targ = get_model_accuracy(model, test_df, ohe, "chess", TARGET_NAME, FEATURE_NAMES)
    train_acc, train_y_pred, train_y_targ = get_model_accuracy(model, train_df, ohe, "chess", TARGET_NAME, FEATURE_NAMES)
    
    print("[" + model_name + "] Test accuracy: ", test_acc)
    print("[" + model_name + "] Training accuracy: ", train_acc)

    # cf_matrix = confusion_matrix(test_df[TARGET_NAME], test_y_pred)

    # using DTrimarchi's file to make a confusion matrix
    # make_confusion_matrix(cf_matrix, ['True Neg','False Pos','False Neg','True Pos'], 'auto', True, True, True, True, True, True, None, 'Blues', 'Decision tree to determine if it is a drugs related stop')

    # if model_name is not 'dummy':
        # plt.savefig("../graphs/[" + model_name + "]-confusion_matrix")
    tree.plot_tree(model, max_depth=3,
                   class_names=TARGET_NAME,
                   filled=True)
    plt.title('Player Decision Tree')
    # plt.show()
    plt.savefig("../graphs/chess_decision_tree")

if __name__ == "__main__":
    print("Decision Tree")
    decision_tree()
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

def plot_multiclass_fig_2D():
    """
    Example function to plot 2D points of different colours
    """
    ### construct the dataframe that we'll plot    
    ### plot the graph:
    fig, ax = plt.subplots()
    
    df = get_chess_df()
    df_new = df[["result","elo_diff", "time_since_gm_diff", "gm_age_diff", "age_diff"]]


    # define the color mapping
    color_mapping = {
        '-1': "red",
        '0': "blue",
        '1': "green",
    }

    # define the label mapping
    label_mapping = {
        "Draw",
        "Black wins",
        "White wins"
    }

    # drop the unneeded columns and rows
    df_new.dropna()

    # for each class
    for cls in ['0','-1','1']:
        # get the examples of that class
        examples = df_new[df_new['result'] == cls].to_numpy()
        print(examples)
        # and then plot it with the color of our liking
        Xs = examples[:, 1] # get all rows from column 0 (elo_diff)
        Ys = examples[:, 2] # get all rows from column 1 (time_since_gm_diff)
        # for running different tests
        ax.scatter(Xs, Ys, c=color_mapping[cls], alpha=0.3) # c: color

    # title, axes
    ax.set_title("Scatter Plot")
    ax.set_xlabel("elo_diff")
    ax.set_ylabel("time_since_gm_diff")

    ax.legend(labels=label_mapping)
    
    # save the figure
    plt.savefig("../graphs/2d-scatter")

def plot_multiclass_fig_3D():
    df = get_chess_df()
    df_new = df[["result","elo_diff", "time_since_gm_diff", "gm_age_diff", "age_diff"]]

    """
    Example function to plot 3D points of different colours
    """
    ### construct the dataframe that we'll plot    
    ### plot the graph:
    ax = plt.axes(projection='3d') # Creating a 3D axes instead of 2D like usual
    
    # define the color mapping
    color_mapping = {
        '-1': "red",
        '0': "blue",
        '1': "green",
    }

    # define the label mapping
    label_mapping = {
        "Draw",
        "Black wins",
        "White wins"
    }

    # drop the unneeded columns and rows
    df_new.dropna()

    # for each class
    for cls in ['-1', '0', '1']:
        # get the examples of that class
        examples = df_new[df_new['result'] == cls].to_numpy()
        # and then plot it with the color of our liking
        Xs = examples[:, 1] # get all rows from column 0 (elo_diff)
        Ys = examples[:, 2] # get all rows from column 1 (time_since_gm_diff)
        Zs = examples[:, 3] # get all rows from column 2 (gm_age_diff)
        ax.scatter3D(Xs, Ys, Zs, c=color_mapping[cls]) # c: color

    # title, axes
    ax.set_title("Scatter Plot")
    ax.set_xlabel("Elo Difference")
    ax.set_ylabel("Time Since GM Difference")
    ax.set_zlabel("Age they became GM difference")

    ax.legend(labels=label_mapping)
    
    # save the figure
    plt.savefig("../graphs/3d-scatter.png")


def svm(model_name="svm"):
    TARGET_NAME = "result"
    FEATURE_NAMES = ["elo_diff", "time_since_gm_diff"]
    model, ohe, train_df, test_df = get_trained_model("chess", model_name, TARGET_NAME, FEATURE_NAMES)
    test_acc, test_y_pred, test_y_targ = get_model_accuracy(model, test_df, ohe, "chess", TARGET_NAME, FEATURE_NAMES)
    train_acc, train_y_pred, train_y_targ = get_model_accuracy(model, train_df, ohe, "chess", TARGET_NAME, FEATURE_NAMES)
    
    print("[" + model_name + "] Test accuracy: ", test_acc)
    print("[" + model_name + "] Training accuracy: ", train_acc)

    # examples = df.to_numpy()
    # X = examples[:, :2]
    # y = df['Class']

    # def make_meshgrid(x, y, h=0.02):
    #     x_min, x_max = x.min() - 1, x.max() + 1
    #     y_min, y_max = y.min() - 1, y.max() + 1
    #     xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    #     return xx, yy
    
    # def plot_contours(ax, clf, xx, yy, **params):
    #     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    #     Z = Z.reshape(xx.shape)
    #     out = ax.contourf(xx, yy, Z, **params)
    #     return out
    
    #  # define the label mapping
    # label_mapping = {
    #     "Win",
    #     "Loss",
    #     "Draw"
    # }

    # clf = model.fit(X, y)

    # fig, ax = plt.subplots()
    # # title for the plots
    # title = ('Decision surface of linear SVC for determining banknote forgery')
    # # Set-up grid for plotting.
    # X0, X1 = X[:, 0], X[:, 1]
    # xx, yy = make_meshgrid(X0, X1)

    # plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
    # ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    # ax.set_ylabel('Skewness')
    # ax.set_xlabel('Variance')
    # # ax.set_xticks(())
    # # ax.set_yticks(())
    # ax.set_title(title)
    # ax.legend(labels=label_mapping)
    # # plt.show()
    # # using DTrimarchi's file to make a confusion matrix
    # # make_confusion_matrix(cf_matrix, ['True Neg','False Pos','False Neg','True Pos'], 'auto', True, True, True, True, True, True, None, 'Blues', 'Logistic refression to determine if driver is arrested')

    # if model_name is not 'dummy':
    #     plt.savefig("../graphs/chess_svm.png")

if __name__ == "__main__":
    print("SVM")
    svm()
    # plot_multiclass_fig_3D()
    # plot_multiclass_fig_2D()
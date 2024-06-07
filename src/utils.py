import joblib
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


def update_model(model : Pipeline)-> None:

    joblib.dump(model , 'models/model.pkl')

def save_metrics_report(
        train_score: float,
        test_score: float,
        model: Pipeline) -> None:
    with open('report.txt', 'w') as report_file:
        report_file.write('Description Model:\n')
        for key, value in model.named_steps.items():
            report_file.write(f'- {key}: {value.__repr__()}\n')
        
        report_file.write('\nScores:\n')
        report_file.write(f'Train Score: {train_score}\n')
        report_file.write(f'Test Score: {test_score}\n')


def plot_metrics_report(Y_test, y_predt):

    cm =confusion_matrix(Y_test, y_predt)
    display_labels = ['BARBUNYA' , 'BOMBAY' , 'CALI' , 'DERMASON' , 'HOROZ' , 'SEKER' ,'SIRA']        
    disp = ConfusionMatrixDisplay(confusion_matrix = cm,display_labels=display_labels)
    disp.plot(cmap="gray")
    plt.xticks(rotation=45)
    plt.grid(False)
    plt.savefig('Prediciton_behavior.png')


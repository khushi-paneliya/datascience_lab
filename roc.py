import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Actual values (1 = disease and 0 = Healthy)
y_actual = [1, 1, 0, 0, 1]

# Predicted probabilities
y_probability = [0.90, 0.50, 0.70, 0.40, 0.30]

# Calculate AUC
fpr, tpr, thresholds = roc_curve(y_actual, y_probability)
roc_auc = auc(fpr, tpr)
print("FPR: ", fpr)
print("TPR: ", tpr)
print("Thresholds: ", thresholds)
print("AUC: ", roc_auc)

# Plot ROC Curve
plt.plot(fpr, tpr, marker = 'o')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

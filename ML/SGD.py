import numpy as np
import matplotlib.pyplot as plt


def mean_squared_error(y_true, y_predicted):
    # Calculating the loss or cost
    cost = np.sum((y_true - y_predicted) ** 2) / len(y_true)
    return cost


# Gradient Descent Function
# Here iterations, learning_rate, threshold
def gradient_descent(x, y, iterations=1000, learning_rate=0.0001, threshold=1e-6):
    # Initialization
    current_weight = 0.1
    current_bias = 0.01
    iterations = iterations
    learning_rate = learning_rate
    n = float(len(x))
    costs = []
    weights = []
    previous_cost = None

    # Estimation of optimal parameters
    for i in range(iterations):
        # Making predictions
        y_predicted = (current_weight * x) + current_bias
        # Calculating the current cost
        current_cost = mean_squared_error(y, y_predicted)

        # If the change in cost is less than or equal to the threshold, stop the gradient descent
        if previous_cost and abs(previous_cost - current_cost) <= threshold:
            break
        # next iteration current will be previous
        previous_cost = current_cost

        # saving cost and weights at each iteration
        costs.append(current_cost)
        weights.append(current_weight)

        # Calculating the gradients
        weight_derivative = -(2 / n) * sum(x * (y - y_predicted))
        bias_derivative = -(2 / n) * sum(y - y_predicted)

        # Updating weights and bias
        current_weight = current_weight - (learning_rate * weight_derivative)
        current_bias = current_bias - (learning_rate * bias_derivative)

        # Printing the parameters for each 1000th iteration
        print(f"Iteration {i + 1}:\t Cost {current_cost:.2f},\t "
              f"Weight: {current_weight:.2f},\t Bias: {current_bias:.2f}")

    return current_weight, current_bias


def main():
    # Data
    X = np.array([32.50234527, 53.42680403, 61.53035803, 47.47563963, 59.81320787,
                  55.14218841, 52.21179669, 39.29956669, 48.10504169, 52.55001444,
                  45.41973014, 54.35163488, 44.1640495, 58.16847072, 56.72720806,
                  48.95588857, 44.68719623, 60.29732685, 45.61864377, 38.81681754])
    Y = np.array([31.70700585, 68.77759598, 62.5623823, 71.54663223, 87.23092513,
                  78.21151827, 79.64197305, 59.17148932, 75.3312423, 71.30087989,
                  55.16567715, 82.47884676, 62.00892325, 75.39287043, 81.43619216,
                  60.72360244, 82.89250373, 97.37989686, 48.84715332, 56.87721319])

    # Estimating weight and bias using gradient descent
    estimated_weight, estimated_bias = gradient_descent(X, Y, iterations=2000)
    print(f"Estimated Weight: {estimated_weight:.2f}\n"
          f"Estimated Bias: {estimated_bias:.2f}")

    # Making predictions using estimated parameters
    Y_pred = estimated_weight * X + estimated_bias
    # Plotting the regression line
    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, marker='o', color='red')
    plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='blue', markerfacecolor='red',
             markersize=10, linestyle='dashed')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if __name__ == "__main__":
    main()

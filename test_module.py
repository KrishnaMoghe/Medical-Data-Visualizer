import unittest
import medical_data_visualizer
import matplotlib as mpl
import numpy as np

# the test case
class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        # Access the first Axes object if multiple are returned
        if isinstance(self.fig.axes, (list, np.ndarray)):
            self.ax = self.fig.axes[0]  # Access the first Axes object
        else:
            self.ax = self.fig.axes  # If it's a single Axes object, use it directly
    
    def test_bar_plot_number_of_bars(self):
        # Flatten axes and iterate through all Axes, filtering out any non-Axes objects
        flattened_axes = [ax for ax in np.ravel(self.fig.axes) if isinstance(ax, mpl.axes.Axes)]
        
        # Count all Rectangle patches in the Axes
        actual = sum(len([rect for rect in ax.patches if isinstance(rect, mpl.patches.Rectangle)]) for ax in flattened_axes)
        
        expected = 22
        self.assertEqual(actual, expected, "Expected a different number of bars in the chart.")

class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_labels(self):
        actual = [label.get_text() for label in self.ax.get_xticklabels()]
        expected = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(actual, expected, "Expected heat map labels to be 'id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight'.")
    
    def test_heat_map_values(self):
        actual = [text.get_text() for text in self.ax.texts]  # Use self.ax.texts to get all text elements
        expected = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0']
        self.assertEqual(actual, expected, "Expected different values in heat map.")
        self.maxDiff = None

if __name__ == "__main__":
    unittest.main()

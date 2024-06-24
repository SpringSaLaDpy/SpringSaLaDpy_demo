from SpringSaLaDpy.Visualization import *
from SpringSaLaDpy.data_locator import data_file_finder
from SpringSaLaDpy.display_info import *
from SpringSaLaDpy.Project_reader import Describe_input_file
from SpringSaLaDpy.MolDraw.MolDraw_exec import display_molecules

#Create the relative path to your desired SIMULATIONS or FOLDER directory
search_directory = os.path.join('Examples','Nephrin-Nck-NWasp', 'Final_version_test_SIMULATIONS', 'Simulation0_SIM_SIMULATIONS')

#Get a description of the input file in that directory

#add flag: skip_links
Describe_input_file(search_directory, links=False, reactions=True, kinetics=True)

display_molecules(search_directory)

#Choose a file in the data folder by giving a search term (some part of the file name) or the full file name
path = data_file_finder(search_directory, ['data'], search_term='BondCounts', file_name=None)
file_info(path, list_neighbors=True)

#Plot the selected data over time
Plotter.plot(path)

#Get a list of columns and their respective indicies
column_info(path)

#Select only the columns you want to see graphed
Plotter.plot(path, [1, 2, 5])

#Change the data file
path = data_file_finder(search_directory, ['data'], 'MoleculeCounts')
column_info(path)
Plotter.plot(path, [3,6,9])

#Show the average Z position of each molecule
Average_z_pos.plot(search_directory, indicies=[], verbose=True, legend_right=True, list_options=True, mode='mol', fill=True)

#Shorten legend with Verbose=False and set list_options=False so only the graph is displayed
Average_z_pos.plot(search_directory, indicies=[0,1], verbose=False, legend_right=False, list_options=False, mode='mol', fill=True)

#View radius of gyration and bonds per molecule distribution (shows last data point by default)
Spatial_Analysis.plot(search_directory, times=[])

#Select a specific point in time
Spatial_Analysis.plot(search_directory, [0.002, 0.004])

#View cluster size distribution histogram at a particular point in time with or without bins
Histogram.plot(search_directory, [], 0.02)
Histogram.plot(search_directory, [1,5,10], 0.04)

Cluster_comp.plot(search_directory, 0.02)

Bound_fraction.plot(search_directory, [0.02])

#data_selection options are 'rg' (cluster radius of gyration), 'cs' (cluster size or number of molecules in a cluster), and 'mr' (maximum cluster radius relative to cluster COM)
#indicies selects maximuim (0), average (1), or both in the plot below. It's both by default
#Warning: computationally intensive for larger simulations
Spatial_Analysis.time_course(search_directory, data_selection='rg', indicies=[0,1], size_threshold=1)
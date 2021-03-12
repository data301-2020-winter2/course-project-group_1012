## Task 5 Analysis

### **Research Question**
Which region has the highest rise in temperature throughout the year? 

### **What we did**
*Loading Data*

To answer our research question, we loaded the data using our first method chain to keep helpful information by removing the null values. 

*Grouping cities into regions*

After dropping null values, we simplified our data by grouping the different cities into their regions using our second method chain. The method chain calculates the mean and combines all the cities into a region. The regions were divided into:
 - British Columbia 
 - The Prairie Provinces
 - Ontario 
 - Quebec 
 - The Atlantic Provinces 
 - The Northern Provinces
This simplifies the data as it summarizes the dataset, allowing us to analyze the data. 

*Filtering Temperature Data by Month*

To further simplify the data, we created a graph to display each region's temperature in a given month throughout the years. We did this by utilizing the melt() function to create a new dataset that allows us to use the hue() function in creating our line graph. The graph allows us to analyze the data to answer our research question through the graph as it presents the changes in temperature in a straightforward manner. 

*Describing the dataset*

Since the graph only showed us the temperature changes trend, we used the describe() function to get a precise number in the change of temperature. 

### **Our Analysis**


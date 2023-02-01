# On the Robustness of Code Generation Techniques: An Empirical Study on GitHub Copilot

In this work we present an empirical study on the robustness of code generation techniques focusing on the novel <a href="https://copilot.github.com">GitHub Copilot</a>.
In this regard, the study has been conducted targeting java as programming language.

----------------

### The repo is organized as follow:

* The folder <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Code">Code</a> contains two subfolder, <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Code/pre-processing">pre-processing</a> and <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Code/post-processing">post-processing</a>
  <br>
  * Under <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Code/pre-processing">pre-processing</a>, you can find the scripts we used to create the paraphrased descriptions (i.e, Pegasus and Translation Pivoting). 
    <br>
  * Under <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Code/post-processing">post-processing</a>, we provide the scripts that have been used to extract the generated results and the script to compute the quantitative metrics.

* The folder <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Dataset">Dataset</a> contains the dataset we built and we used to run the experiments.

* The folder <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Figures">Figures</a> contains the same histogram and box plots we reported in our paper, with the difference being the code context: *Non Full Context* code representation.


* The folder <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Results"> Results </a> contains two subfolder, <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Results/Full-Context">Full-Context</a> and <a href="https://github.com/antonio-mastropaolo/robustness-copilot/tree/main/Results/Non-Full-Context">Non-Full-Context</a> in which we share the results of the experiments including the generated java instances, namely *Original, Pegasus, and Pivoting.*
* Note that we also make available the Apple Scripts we used to run Copilot on our dataset automatically. Specifically, we created one script for each instance, meaning that we have more than 5K apple scripts collected and stored within the relative index folder within the Copilot-Run.zip file.


* You can also find the results concerning the manual analysis we performed to assess the equivalence of the automatically generated paraphrased descriptions:
    - <a href="https://drive.google.com/file/d/1giSaKDvYsoNeXL216PaJkXq_fHeMSJb8/view?usp=sharing">Pegasus</a>
    - <a href="https://drive.google.com/file/d/16-18GmG5PrKjV6f78vIr98Q2gyJAe9lP/view?usp=sharing">Translation-Pivoting</a>



----------------

Finally, we also release the maven projects (RAW DATA) that have been used in this study here: <a href="https://drive.google.com/drive/folders/1ud-tQlaUfyrDefCXd1PzSJnJQzcS6lJF?usp=sharing">:open_file_folder:</a>

<b><i>NB: For each project, we store the test suite results when running copilot on the variations of the code descriptions. In detail, you will find several text files reporting the results after the test suite has been run for each project folder, considering that specific instance. E.g., *result_test_robustness_WorkflowRemoverTest_parseParameters_Original.txt* contains the results of the parseParameters method with the original code summary, whose test case can be found in the test class WorkFlowRemoverTest..</i>
</b>

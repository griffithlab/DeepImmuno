[![Stars](https://img.shields.io/github/stars/frankligy/DeepImmuno)](https://github.com/frankligy/DeepImmuno/stargazers)


# DeepImmuno
Deep-learning empowered prediction and generation of immunogenic epitopes for T cell immunity. 

We recommend to try out our web application for that: https://deepimmuno.research.cchmc.org

The repository for building the DeepImmuno web server: https://github.com/frankligy/DeepImmuno-web

- Please refer to [DeepImmuno-CNN](#deepimmuno-cnn) if you want to predict immunogenicity

- Please refer to [DeepImmuno-GAN](#deepimmuno-gan) if you want to generate immunogenic peptide

- Please refer to [Train your own GAN](https://github.com/frankligy/DeepImmuno/tree/main/extension) if you want to generate peptides with customized features/properties.

Enjoy and don't hesitate to ask me questions (contact at the bottom), I will be responsive! Feel free to raise an issue on github page!

## Installation

```
pip install git+https://github.com/griffithlab/DeepImmuno.git
```

## Citation
If you find that tool useful in your research, please consider citing our paper:

*DeepImmuno: deep learning-empowered prediction and generation of immunogenic peptides for T-cell immunity*, Briefings in Bioinformatics, May 03 2021 (https://doi.org/10.1093/bib/bbab160)

## Reproduce
All the codes for reproducing figures in the manucript can be accessed in [`/reproduce/fig`](https://github.com/frankligy/DeepImmuno/tree/main/reproduce/fig)

## FAQ
1. **Why I get zero immunogenicity score when running on deepimmno webserver?**

Currently, Deepimmuno-CNN only supports peptides in the length of 9 and 10. We are working on adding support to peptides of other length and it will be available in the future version. But for now, it is advisable to filter to your queried peptides to 9mer and 10mer. 

2. **How did I obtain the paratope information to encode the HLA?**

I compile a [README.md](./new_imgt_scraping/README.md) file for all the detailed steps, feel free to contact me if you have any confusions.

3. **Can I retrain the CNN model?**

Please refer to [cnn_retrain_notebook.ipynb](./reproduce/cnn_retrain_notebook.ipynb) for the instructions. Feel free to reach out if I can help with anything!

4. **How to derive immunogenicity potential?**

Imagine we have a dataframe named `data`, each row is a peptide-MHC complex, it has two column, one is `test`, another is `respond`, which records number of times
the pMHC was tested and the number of times the immunogenicity response was observed. With that, you can refer to function `assign_posterior` in [here](https://github.com/frankligy/DeepImmuno/blob/main/src/immuno3_3.py#L17-L43) to derive immunogenicity
potential.

5. **Could you provide an useable graph neural net codebase?**

I added a [notebook](./reproduce/reproduce_gcn.ipynb) to run GCN model, however, as we illustrated in the paper, the GCN model in this case, doesn't achieve a good performance which we 
attribute to the "short-cut" learning. If you want to improve the model, I may suggest to start thinking how to better encode the HLA-peptide interaction as a graph, what would be the proper
edge weight. Hoping that could be helpful.

6. **How Does the placehoder amino acid's embedding be calculated?**

After reading the AAindex for the 20 amino acid, we have a matrix of the shape 20 * 566, then we take the mean of these 20 amino acid to serve as the embedding of the 21st amino acid "X" to arrive at the final matrix of the shape 21 * 566. The code is available [here](https://github.com/frankligy/DeepImmuno/blob/8d0d14900cd9f183d0795ab4b1b4f8dcb89a85e2/src/utils_get_afterpca.py#L177).

7. **Where can I find the training and testing dataset?**

* [Training dataset](https://github.com/frankligy/DeepImmuno/blob/main/reproduce/data/remove0123_sample100.csv)

This dataset was downloaded from IEDB, immunogenicity is based on the submitter's annotation, and we collected the number of samples tested, and the number of samples that responded to derive the immunogenicity potential for training the regression model (detail can be found in the paper and supplemental methods)

* [Dengue dataset](https://github.com/frankligy/DeepImmuno/blob/main/reproduce/data/dengue_test.csv)

* [TESLA Tumor Neoantigen dataset](https://github.com/frankligy/DeepImmuno/blob/main/reproduce/data/ori_test_cells.csv)

The first four columns are the original data information

* [SARS-CoV-2 dataset](https://github.com/frankligy/DeepImmuno/blob/main/reproduce/data/sars_cov_2_result.csv)

Immunogenicity-con and immunogenicity-un represent whether the test is conducted in convalescent or unexposed subjects.


## DeepImmuno-CNN

#### Dependencies

python = 3.6

tensorflow = 2.3.0

numpy = 1.18.5

pandas = 1.1.1


- *Note: This is the enviroment that I used for development and I also tested it. But as long as you use python > 3, tensorflow = 2.3, It should also work.*

#### How to use?

If you want to query a single epitope (peptide + HLA), for example you want to query peptide _**HPPLMNVER**_ along with _**HLA-A*0201**_. You need to

```shell
deepimmuno-cnn --mode "single" --epitope "HPPLMNVER" --hla "HLA-A*0201"
```

If you want to query multiple epitopes, you just need to prepare a csv file like this:

```shell
AAAAAAAAA,HLA-A*0201
CCCCCCCCC,HLA-B*5801
DDDDDDDDD,HLA-C*0702
```

Then you run:

```shell
deepimmuno-cnn --mode "multiple" --intdir "/path/to/above/file" --outdir "/path/to/output/folder"
```

- *Please note, when you specify the output dir, don't include the forward slash at the end, for example, use "/Desktop" instead "/Desktop/"*

A full help prompt is as below:

```
usage: deepimmuno-cnn [-h] [--mode MODE] [--epitope EPITOPE] [--hla HLA]
                         [--intdir INTDIR] [--outdir OUTDIR]

DeepImmuno-CNN command line

optional arguments:
  -h, --help         show this help message and exit
  --mode MODE        single mode or multiple mode
  --epitope EPITOPE  if single mode, specifying your epitope
  --hla HLA          if single mode, specifying your HLA allele
  --intdir INTDIR    if multiple mode, specifying the path to your input file
  --outdir OUTDIR    if multiple mode, specifying the path to your output folder
```

## DeepImmuno-GAN

#### Dependencies

python = 3.6

pytorch = 1.4.0

numpy = 1.18.4

pandas = 1.0.5


- *Note: This is the enviroment that I used for development and I also tested it. But as long as you use python > 3, pytorch = 1.4, It should also work.*


#### How to use

Pretty simple, just run like this

```shell
deepimmuno-gan --outdir "/path/to/store/output"
```

It will automatically genearte one batch, which is **64** pseudo-immunogenic peptides of **HLA-A*0201** for your. It is worth noting that, because of the way I encode the peptide, there will be a placeholder "-". 

A full help prompt is as below
```
usage: deepimmuno-gan [-h] [--outdir OUTDIR]

DeepImmuno-GAN to generate immunogenic peptide

optional arguments:
  -h, --help       show this help message and exit
  --outdir OUTDIR  specifying your output folder
```

- *Please note, when you specify the output dir, don't include the forward slash at the end, for example, use "/Desktop" instead "/Desktop/"*

## Contact

Guangyuan(Frank) Li

li2g2@mail.uc.edu

PhD student, Biomedical Informatics

Cincinnati Children's Hospital Medical Center(CCHMC)

University of Cincinnati, College of Medicine






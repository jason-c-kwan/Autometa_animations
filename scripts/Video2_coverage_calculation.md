Video 2 - Coverage calculation
=======

Scene 1 - Title screen
-------

```
The Autometa logo is animated and then extra text is written so that the screen reads:
How Autometa Works
2. Coverage calculation
```

This is the second video in a series that explores how Autometa works to separate genomes from metagenomes, a process known as "binning". This time, I will explain the different ways that coverage can be calculated, and how Autometa uses this information.

```
Stuff on the screen fades out
```

Scene 2 - Why coverage is useful
------

```
The words "Why do we calculate coverage?" appear when mentioned
```

But before we get into that, we have to answer the question, why do we need to calculate coverage in the first place? 

```
Those previous words disappear and then we show a bulletted list:
* Nucleotide composition
* Taxonomy
* Coverage/abundance (a box is drawn around this as it is mentioned)
```

Well the first thing to know is that Autometa uses three basic characteristics of contigs to separate and classify them - the nucleotide composition, their inferred taxonomy and, finally, the coverage, which is a proxy for the abundance of that sequence in the parent DNA sample.

```
That previous stuff disappears and we show a 2D BH-tSNE plot. Hopefully one can be found that contains at least two genomes that overlap but have different coverages.
```

Now, we will go into all the other aspects of how Autometa separates contigs in other videos, but when we separate contigs on the basic of nucleotide composition, what we are doing is to collapse 5-mer frequencies in each contig to just two dimensions using a technique known as dimension reduction. Here is an example of what some contigs in a metagenome look like on these two dimension.

```
One of the groups is circled, and we write the number of markers (and % single copy) and the derived completeness and purity.
```

Now another thing that Autometa does during the clustering step is that it checks the completeness and purity of bins, and it rejects ones that are very incomplete and/or very impure. It does this by finding marker genes known to only occur as single copies in bacterial genomes. This bin has mostly single copies of most of the expected markers, and so it is both highly complete and pure.

```
We circle another bin, showing high completeness but also high impurity
```

This other bin, though, seems to have a lot of redundant markers and so it looks like there might be contigs from more than one genome in this group. Why would this occur? Well, closely related genomes are expected to also have similar nucleotide composition, and so we would expect closely related species to overlap on this type of plot.

```
The plot rotates so that we see the z axis (coverage), and separation of the component bins of the previously circled one. Perhaps the circle becomes a cylinder?
```

But, if we use coverage as the third dimension, we can now see that our previous circle encompases a cylinder which contains multiple groups which have similar nucleotide composition.

```
The cylinder disappears and we circle the different component groups, showing their respective completeness and purities.
```

And we can see that each group by itself is much more pure than the 2D group, and so using coverage is crucial if you think you might have closely related species in your metagenome.

```
Everything disappears
```

Scene 3 - How do we calculate coverage?
-------

```
The title "How do we calculate coverage?" appears, underlined
```

But how do we calculate coverage? Well, in Autometa there are two choices.

```
We show the following text:
1. Extract from contig names

[We also show an example spades type name]
```

The first way is you can extract the coverage from your contig names, assuming you used Spades as your assembler or any other assembler which gives the contig names in this format. If you are unsure if this applies to you, have a quick look at the contig headers in your assembly fasta file, and see if the names look like this.

```
We show another list item:
2. Calculate by read alignment
```

The other choice is to have Autometa calculate coverage itself through aligning your reads. Now in addition to this taking more compuation time there are few things to keep in mind when choosing which one you want to do.

```
By 1, we show:
<- don't need the reads
By 2, we show:
<- need access to reads
```

The first is that when choosing option 2 you need to have access to the original reads used to make the assembly in the first place. With option 1, Autometa doesn't need to ever look at the reads.

```
Those last parts disappear.

By 1, we show:
<- k-mer coverage

By 2, we show:
<- read coverage
```

The second thing to be aware of is that assemblers such as spades don't report conventional nucleotide or read coverage in the contig names, but rather the coverage in terms of unique k-mers they have used to make the de bruijn graph of the assembly. 

```
We show the equation:

Ck = C (L - k + 1)/L
```

The k-mer coverage, or Ck is related to the nucleotide coverage, or C, based on this equation, and the relationship also depends on the read length, or L, and the k-mer size, or k. So the k-mer coverage is always some fraction of nucleotide coverage because the k-mer size used by the assembler will be smaller than the read length of the dataset.

```
Everything disappears
```

Scene 4 - Outro
----

```
We show the Autometa github URL
and the readthedocs link
```

So that's all we have for this video. If you have any questions about how to use Autometa you can find the documentation at autometa dot readthedocs dot org, and if you are having trouble running it, you can submit an issue at our Github repository, where you can also download the source code.

```
Those links move up and then we show the NSF logo and the grant number
```

We also gratefully acknowledge NSF for funding the development of Autometa, under DBI grant number 1845890.


Video 1 - Length filtering
===================

Scene 1 - Title screen
-------
```
The autometa logo is animated and then extra text is written so that the screen reads:
How Autometa Works
1. Length filtering
```

This is the first video in a series that explores how Autometa works to separate genomes from metagenomes, a process known as "binning". In particular, we will go through why we initially filter an assembly by contig length.

```
Stuff on the screen fades out
```


Scene 2 - What to do before starting Autometa
------
```
We write the following title: "Before you begin" (underlined)
```

But before we go into that, let's just briefly go into what you will need to do before you start using Autometa. 

```
Pictures of mixed bacteria appear, with visible genomes
```

When we do a metagenomic experiment, we take a sample directly from an environment of interest, that will invariably have a mixture of lots of different types of microorganisms. We might not know what the types are or how many there are. 

```
We show the genomes of each bacterium (cells dissapear)
```

The next step is to extract the total DNA from all organisms present in the sample,

```
We show an arrow going through a picture of a sequencer and going to a collection of short reads
```

...then to subject it to shotgun or random sequencing. Because metagenomes often contain many different genomes, you typically have to do a lot more sequencing than for an isolated single microorganism. Current sequencing platforms differ in the length and accuracy of the sequence data they produce, but they generally produce a large number of small sequences called...

```
We add the word "reads" under the diagram of reads
```

..."reads". The point is that each read is much shorter than a genome, and so we need to work out how the reads overlap to produce longer contiguous sequences called "contigs".

```
A lot of the stuff on the screen fades out, leaving the reads, which go to the left hand side, with an arrow going to a collection of longer sequences with reads aligned, with the label "contigs".
```

This process is known as...

```
We write the word "assembly" over the arrow
```

...assembly, and it is not carried out by Autometa, but rather a specialized assembler. Links to some assemblers can be found in the description below. 

Scene 3 - Assembly characteristics
------
```
Everything but the contigs from the previous scene disappear, and the contigs move to the center of the screen
```

It's highly unlikely that any one genome in the metagenome will assemble into one contig covering the whole genome, and even if this were to happen, you won't know if any contig is complete or part of another genome. The process of examining the contigs in a metagenome and deciding which ones are actually part of the same genome is called "binning", and it is what Autometa is designed to do. 

```
The contigs rearrange into descending order of length, with a Y axis that is labelled "length"
```

Another thing to be aware of is that an assembly will contain contigs of varying length. 


```
We highlight some of the shorter contigs
```

If a genome contains a lot of repeats or it is closely related to other species present in the sample that have genomes with similar sequences, the assembler can get confused and it won't be able to reconstruct very long contigs. 

```
We highlight some of the longer contigs
```

Other times, a genome could contain few repeats and there are no other closely related species in the sample, in which case the assembler is able to construct contigs that are quite long. But how do we measure the _overall_ quality of a metagenomic assembly? Well, one way we can do this is to order the contigs in descending order of length, ...


```
We show a bar graph with two sides, and a scale from 0-50%. As the lines change color, a live figure of > x bp updates along with the size of the graph and the %, until we are over 50%
```

...and count up the total length as we go in descending order of length. When we reach 50% of the total length of the assembly, we call the length of the smallest contig in our counted set...

```
We change > x bp to x bp = N50
```

...the N50, and the larger this number is, the more longer contigs you have, although you always will have some amount of short contigs. 

```
The shortest contigs are highlighted with a box and the text "< 3 kbp" appears
```

In Autometa we have the option to discard the shortest contigs, and you can specify the length cutoff you would like. But why is this useful or necessary?

Scene 4 - Taxonomy limitations
------

```
Everything but one of the small and one of the large contigs disappears, and it changes to a
horizontal orientation in the middle of the screen. Arrows appear above the contigs, signifying genes
```

The first reason why it is a good idea to discard short contigs before binning is that taxonomic classification will be less accurate for short contigs. For more details, see our video on how Autometa classifies contigs taxonomically, but the gist of it is that we search predicted protein-coding sequences in contigs, shown as arrows here, against sequence databases.

```
We show some classifications by the genes in the two contigs. Colors of the arrows change accordingly. The middle gene of the short contig should be a different classification, and some of the long one as well.
```

If genes have sequences very similar to database sequences, we can classify them down to the species, but if they are very divergent we might not be able to classify them very accurately. 

```
We show the various classifications from the large and small contig turning into a "vote" which
goes into ballot boxes
```

Autometa takes the classifications for each predicted gene, and employs a vote system to decide upon the correct classification for the contig. 

```
The large contig and ballot box disappears, and we center the small contig, ballot box and the result of the vote.
```

The problem with including short contigs is that the vote can be unduly influenced by a small number of genes, just like an election with a low turnout can be influenced with a smaller number of votes.

```
We show an arrow going to the outlier gene with the text 'horizontal gene transfer'
```

For instance, if a short contig happens to have a gene that was recently obtained through horizontal transfer, the contig might be misclassified.

```
The text showing 'horizontal gene transfer' turns into 'secondary metabolism'
```

There are also certain types of genes which are hardly ever classified with the proper taxonomy, such as secondary metabolite genes, which vary greatly within taxonomic groups and are frequently horizontally transferred.

```
Everything disappears
```

Scene 5 - K-mer accuracy
------

```
We show a short part of a contig sequence, and then animate the meaning of 5-mers
```

The second reason why we should discard short contigs is that k-mer counting becomes inaccurate for shorter contigs. We have another video on how Autometa does k-mer counting, so we'll just go over the basics right now.

```
We add the text "1,024 possible 5-mers"
```

By default, Autometa uses a K-mer size of 5, and there are 1024 possible 5-mers. We compare the nucleotide compositions of contigs by looking at the differences in the frequencies of all of these 1,024 possible 5-mers. 

```
We label the k-mer currently highlighted as "A"
```

Let's say we call the 5-mer with the sequence XXXXX "A". And let's say that in one particular genome in your metagenome, A is particularly rare, occuring once for every 1,000,000 other k-mers counted. 

```
The picture changes to show a circle representing a chromosome. The text "5 Mbp" appears when mentioned below
```

A typical bacterial chromosome might be 5 megabases in length. We can split this into 5 million 5-mers because they overlap and the chromosome is circular. 

```
We show the locations of 5 "A" 5-mers in the chromosome, two of which are closer together
```

So, on average we would get five instances of "A" in this chromosome. But when we are binning we don't see the complete sequence of chromosomes but rather smaller contigs.

```
We show a small ~1 kbp section without "A", and label "1 kbp 0/1,000 A"
```

If we have a small contig, around 1,000 bp in length, then there is a good chance that we won't find an instance of A, so we don't count any. The observed frequency is 0 out of 1,000, which is actually an undercount.

```
We show another 1 kbp section with one "A", and label "1 kbp 1/1,000 A"
```

But it is not impossible to find an instance of A in a small contig, in which case the 5-mer will be vastly overcounted, in this case as 1 in one thousand instead of 1 in a million.

```
We show a slightly bigger contig around two "A"s, and label "3 kbp 2/3,000 A"
```

It is also not impossible to have multiple instances of "A" in a relatively short contig. In this case our observed count would be 2 out of 3,000.

Scene 5 - Effect of length cutoff on embedding
-------

```
The previous stuff dissapears, as we show a graph of some contigs on axes of GC% and coverage (all the contigs with no length cutoff, all points are grey for now)
```

OK, so let's think about how the length cutoff affects binning in Autometa. Here is a simulated metagenomic assembly containing XXX bacterial genomes, and we are plotting each contig as a point on these axes of GC% and coverage.

```
The coloration changes to indicate the different source genomes
```

If we color the points based on the source genomes, we can see it is quite difficult to separate everything. Also note here that...

```
We add the text "length cutoff = 0 bp"
```

...we aren't applying a length cutoff, so this is everything the assembler spits out. 

```
We start an animation, showing how the points disappear as we increase the length cutoff, up to about 10 kbp, while changing the text appropriately.
```

You can see here that as we increase the length cutoff, we loose more and more contigs, but that you can begin to see that it might be easier to separate genomes. But Autometa doesn't use these axes to cluster the contigs...

```
We transform the 10 kbp cutoff points to the embedded BH-tSNE space
```

Instead it processes the 5-mer counts through a process called dimension reduction or embedding to show nucleotide variance on these two axes. We have another video on the process of dimension reduction, but right now we are going to just consider the effect of the length cutoff on the embedded coordinates. Here we retain a length cutoff of 10 kbp, and you can see that the different genomes are generally well separated. And if you can visually see good separation, then the clustering algorithm should also be able to find the groups without a problem.

```
We start an animation that cycles through the length cutoffs, going down to 0 bp
```

But as we decrease the length cutoff, you can see that adding points where the k-mer count might be more inaccurate has the effect of making the separation less stark, until we have just a cloud of points that would be very difficult to separate into groups if we didn't know the ground truth. 

Scene 6 - Conclusion
------

```
Everything disappears and we show the title "conclusion". We draw a horizontal line labeled "length cutoff", with "short" on the left and "long" on the right.
```

So what does this all mean, and what should you choose as your length cutoff? Well, there are clearly tradeoffs involved.

```
By "short" - write "worse separation"
By "long" - write "better separation"
```

We just saw that you can get worse separation according to nucleotide composition for shorter cutoffs, and better separation for longer cutoffs. However, the tradeoff is...

```
By "short" - inclusive
By "long" - excludes many sequences
```

...that with long cutoffs you are excluding a lot of sequences, and therefore your bins might be incomplete, and with short cutoffs you are not separating very well so your bins could be impure.

```
We show a sort of curve above the line showing completeness (with label), and a curve below the line showing purity (with label). We also show a vertical line intersecting with each moving up and down.
```

Finding the ideal value might take some trial and error. One thing you can do is assess the completeness and purity of the bins you obtain with different settings, and try to find the setting that maximizes both completeness and purity. Another thing you can do is to visualize the embedding coordinates outputted by Autometa, and judge for yourself whether groupings appear discrete or if it seems like there are too many points to pick out groups.

```
Everything disappears
```

Scene 7 - Outro
-----

```
We show the Autometa github URL
and the readthedocs link
```

If you have any questions about how to use Autometa you can find the documentation at autometa dot readthedocs dot org, and if you are having trouble with running it, you can submit an issue at our Github repository, where you can also download the source code.

```
Those links move up and then we show the NSF logo and the grant number
```

We gratefully acknowledge NSF for funding the development of Autometa, under DBI grant number 1845890.





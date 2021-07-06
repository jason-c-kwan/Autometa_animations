Video 3 - ORF Calling
=======

Scene 1 - Title screen
-------

```
The Autometa logo is animated and then extra text is written so that the screen reads:
How Autometa Works
3. ORF Calling
```

This is the third video in a series that explores how Autometa works to separate genomes from metagenomes, a process known as "binning". This time, I will explain how and why we incorporate the calling of ORFs or "open reading frames" into the pipeline.

```
Stuff on the screen fades out
```

Scene 2 - What are ORFs?
------

```
We show the text:
What are ORFs? 
in the center of the screen
```

But before we get into the details, it is worth going over what ORFs are. If you are confident in the biology here, you can of course skip over this part to the next bit of the video. As I said just now...

```
The text morphs to:
What are Open Reading Frames? (with O R and F underlined)
```

...ORF stands for "open reading frame", and to understand what that is, let's look at a short section of a bacterial chromosome.

```
The text disappears and we show a short section of a bacterial sequence (double stranded sequence)
We also label the 5' and 3' ends of each strand
```

You probably know that DNA consists of a sequence of nucleotides, of which there are four, A, T, G and C, 

```
Arrows appear by each strand going in the 5' to 3' direction
```

and that there are two strands which run antiparallel from 5 prime to 3 prime ends. Now, you might also be aware that genes are sections of DNA sequence within a chromosome, and that most genes encode for protein sequences. But how does that work? 

```
We highlight three contiguous nucleotides and label it "codon"
```

Well, a sequence of three nucleotides forms a "codon", which codes either for a specific amino acid, or it is a stop codon.

```
We change the "codon" label to "Ala", and we also highlight a UAA stop codon (or whatever)
```

For instance, the GCT codon here codes for Alanine, and the TAA codon is a stop codon which on an mRNA would signal for the ribosome to release the peptide it has just made. The meaning of all the possible codons has been worked out, and this is called the genetic code. But if I gave you that code table and asked you to go away and tell me what protein this section of DNA makes, you would face a few problems.

```
We reemphasize the antiparallel arrows and add the text:
strand?
```

One thing I didn't mention just now is that the code goes in the 5 prime to 3 prime direction, but we still have a choice of what strand to use. 

```
We make the bottom strand sort of more translucent
```

But let's just say we know in this case that the top strand is the one used for the gene. There is also another question that needs to be answered, which is...

```
We have a vertical down arrow pointing to the first nucleotide of the Ala codon
```

...where do you actually start reading the code? Here we are starting at this G, to read GCU as Alanine, but ...

```
The arrow and the codon move one nucleotide along, the translation changes accordingly.
```

...if we started just one nucleotide further to the left, then the translated amino acid changes. Now let's see how many different ways this sequence can be read.

```
We highlight reading frame 1 codons, and add their translations above the strand, making the amino acids color coded.
```

Here is one translation, starting the first codon at nucleotide 1 as shown here. We call that the first reading frame. And it turns out ...

```
We move the codons one nucleotide along and add their translation above the first one.
We then move the codons one nucleotide along again and add a third translation.
```

...that for one strand of DNA, there are three reading frames. Now, if we bring back the other strand...

```
We fade back in the other strand, then add the three translations as before.
```

...we can see that the second strand also has three reading frames, but they go in the opposite direction. So a double-stranded DNA sequence has six possible reading frames. So with that in mind, let's think about what gene calling is.

```
That stuff moves up a bit and then we write:

Gene calling:
* Where genes are 
* Reading frame
* Translation

[The points will be emphasized as they are mentioned]
```

Essentially gene calling is a computational task which encompases determining where genes are, what reading frame they use, and their protein translation. One of the ways that gene calling programs use to tackle this problem is to look at the stop codons.

```
The text disappears and the DNA sequence goes back to the center, and we fade out all the codons and translations apart from the stop codons.
```

Here we can see that in any particular sequence you will get stop codons every now an again, in different reading frames. And since there are 64 possible codons and there are three stop codons, then a little under 1 in 20 codons will be stop codons in any random sequence.

```
We zoom out the sequence so that it just looks like two lines, and we are showing the stop codons in the same color as vertical lines in each of the six reading frames.
```

However, if the sequence we are looking at is from a bacterial chromosome, then it isn't a random sequence but rather something that evolved over millions of years. Here I am showing the locations of stop codons in each of the three forward and three reverse reading frames. 

```
We highlight one of the gaps in the stop codons, showing how many codons long it is.
```

And since we know that random sequences should have a stop codon every 20 or so codons, a gap between stop codons longer than about 50 codons is considered statistically significant, meaning that it is likely that evolution maintained that deviation from randomness in order to code a protein. 

```
We highlight all the different ORFs
```

These regions with few stop codons are called "open reading frames" or ORFs. In bacteria, a single ORF codes for a complete protein, and there are generally only small spaces between ORFs for things like promoters, and so consequently it is fairly easy to pick out which regions likely constitute protein coding genes. 


Scene 3 - How Prodigal works
------
OK, so at this point I've probably made this sound a bit more easy than it actually is. One problem is that this method of looking at stop codons works really well in chromosomes with low GC content, but some organisms have pretty high GC content in their chromosomes, ...

```
We show a corresponding diagram underneath the one that is already there, of a high GC organism
```

... and since the three stop codons are either 0 or 33% GC, the random chance of seeing stop codons is lower in high GC chromosomes, and it is more difficult to see where the open reading frames actually are. And of course, when we are doing this in Autometa, we also have the problem that we have to do this for thousands or even hundreds of thousands of contigs. 

```
The low GC diagram disappears and above the high GC diagram, we write the text:
Prodigal
https://github.com/hyattpd/Prodigal
```

And within Autometa we actually use a separate gene finding program called Prodigal. 

```
We highlight all the open reading frames from valid start codons to stop codons in the low-GC diagram
```

What prodigal does is that it individually scores each reading frame between a valid start and a stop codon, using things like the GC percent at each codon position and the presence of a Shine-Dalgarno sequence, which is the part of a messenger RNA that binds to part of the ribosome in bacteria. 

```
We show the accepted ORFS, and the others drop away
```

The highest scoring ORFs for a given bit of the chromosome are accepted as Prodigal as probably being the correct protein-coding genes. 

```
Everything disappears
```

Scene 4 - How Autometa uses ORFs
----

```
Text appears:
Why call ORFs during binning?
```

Now, you may be wondering why Autometa calls ORFs during binning, especially since most other binning pipelines don't do this. Well there are three reasons.

```
Question moves up a bit, and then we write:
1. Determining completeness and purity of bins
```

The first is that if we know where the genes are, we can look for special marker genes which we can use to estimate the completeness and purity of bins.

```
We show a broken up circular chromosome, and dots representing markers (labelled) of different colors.
We write:
139/139 [check mark] Complete!
Each single copy = Pure!
```

We have another video about how we use marker genes to do this, but essentially, each one typically only occurs as a single copy in high quality bacterial genomes, and so if they are all there we can say the bin is complete, and if they are all unique single copies then we can say the bin has no contamination. Autometa checks this during binning so that it knows the bins it outputs have a high chance of being of good quality.

```
The diagrams that were just drawn disappear, and we write:

2. Removing eukaryotic contamination
3. Increasing performance in large datasets
```

The two other reasons we call ORFs are sort of connected. It helps us remove eukaryotic contamination, and it also allows Autometa to perform better in large datasets. Now, it's probably not immediately obvious how that would work, so I'll explain.

Scene 5 - Kingdom binning
------

```
We show a contig with arrows beside it representing ORFs
```

When we have identified where ORFs are on the contig, we can take the translated protein sequences...

```
The ORF/contig diagram moves if necessary, and we show curved arrows going from the ORFs to a representation of the NR database
```

...and search them using BLAST against the NR database from NCBI, which is a collection of all the unique protein sequences that have been determined.

```
Most of the curved arrows but one fades slightly, and then we show another arrow going from the database to a list of hits
```

For each of the queries we search against the database, we get a list of similar sequences which BLAST found. We have another video which goes into the details of this process, but for now I'll just say that we look at the assigned taxonomy of the hit sequences and make a judgement as to the likely taxonomy of the query. This takes into account things like how some sequences in NR are found in multiple taxa, and if there are multiple taxa in the hits, then that decreases the certainty with which we can assign a taxa to the query ORF.

```
Other stuff disappears and we move the contig and ORF arrows to the center again, and add ORF taxa
```

After that process we have putative classifications for each ORF in a contig, ...

```
We show a large arrow going to an overall contig classification. It should make somewhat intuitive sense but leave out some of the nuances that will be discussed in the taxon assignment video
```

...and through a voting system we come up with a likely taxon assigment for the contig as a whole, using the individual ORF assignment. Now, even before you check out our detailed video on taxon assignment, some of you will probably be thinking that this is a very crude way of classifying contigs into taxa. And you are right about that. But, the thing to bear in mind here is that Autometa is not directly using this information to separate contigs into bins. Rather, this information is useful to make very broad separations that simplify the data hopefully without splitting up contigs that should be in the same bin.

```
Everything on the screen disappears, and we show two contigs with the classifications:

Bacillus subtilis
Bacillus anthracis

Perhaps we also show a venn diagram with the exact numbers determined from scanning the taxdump files? We could also include two slightly different pictures of bacterial cells
```

For instance, in the NR database there are XXX proteins for which an identical sequence is found in both Bacillus subtilis and Bacillus anthracis. And therefore using BLAST it would be very difficult to tell whether a contig should be classified as subtilis versus anthracis.

```
The two organisms change to the aphid Pentalonia nigronervosa and Buchnera aphidicola (see https://pubmed.ncbi.nlm.nih.gov/33004433/), along with a similar venn diagram as above

(Note: Should probably include references for pictures and genomes
```

However, if organisms are only very distantly related, then their protein sequences are very discriminatory. For instance, the banana aphid, Pentalonia nigronervosa, and its bacterial symbiont Buchnera aphidicola do not share any identical gene sequences [update if necessary], even if there might be other aphid species or bacteria that share sequences from either one. So, the primary way we use this taxonomy information in Autometa is to make broad separations, such as...

```
We show a separation of contigs between eukaryotic and prokaryotic (with the aphid and bacteria)
```

...between eukaryotic and prokaryotic organisms. This is very useful if you are looking at a host associated metagenome. Unless you are studying a very well characterized host, the genome has likely not been sequenced, and Autometa allows you to remove eukaryotic sequences when a reference genome is not available. You might also have a metagenome with substantial eukaryotic contamination. It is worth noting here that a lot of other binning programs assume all the input sequence is prokaryotic, and you can end up with eukaryotic contigs contaminating your bins. 

Scene 6 - Increasing performance
------

```
The previous stuff disappears

We show a group of bacteria, and a separation into different phyla, then class, etc.
```

But we can actually use our taxonomic classifications to make further separations, for example we can separate the bacterial contigs further into different phyla and classes, etc. But, we know that our classifications are not often accurate down to the exact species, so why would this be useful? 

```
We show a fairly simple BH-tSNE plot for not a very complex dataset, colored by species or something

We show the text:
*simulated dataset
```

Well, we will go into this in more detail in the video on taxon assignment, and you will also find more information in the K-mer embedding video. But for now, I'll just say that Autometa uses nucleotide composition to separate contigs, and raw nucleotide sequence frequencies are put through a process called embedding, to give a graph like this. You can see here that the points representing contigs form discrete groups. We have colored the points according to the known species of the sequences, so we can see that the groups represent contigs that should be binned together. Both the human eye and the clustering algorithms that Autometa uses can easily see where the groups are.

```
We transition to a BH-tSNE plot of a much more complex dataset, again, colored by ground truth species
```

However, this task is much more difficult for more complex datasets. Again, we have colored the points according to the species we know they belong to, since this is simulated data, but if you didn't have that information it would be quite difficult to pick out groups here. 

```
Most of the points go grey, and we highlight the "proteobacteria" phylum
```

But, if we have run our taxonomic classification method on these contigs, then we can separate them based on taxonomic group. Here, I have colored just the contigs that are classified in the proteobacteria phylum of bacteria.

```
The grey points disappear and then we re-embed the remaining points
```

If we look at just the proteobacterial contigs separately, we can now see more discrete groups, but it is still a bit crowded. 

```
We highlight just the alphaproteobacteria [can change according to the data], and then re-embedd that
```

So, we can separate further, now just looking at the alphaproteobacteria, for instance. And this is what Autometa does. Basically, if you have taxonomy classification turned on, Autometa first tries to get good bins from the overall data, and then it will then try to split up the data based on taxonomy. First, at the level of phylum and moving down towards species. This has the effect of increasing performance because it is easier to cluster smaller subfractions than it is to work on much larger complicated datasets.

Well, that is basically the end of this video. If you want to find out more about how we use taxonomy information during clustering, you can look at both our taxon assignment and K-mer embedding videos.

```
Everything disappears
```

Scene 7 - Outro
-----

```
We show the Autometa github URL
and the readthedocs link
```

And if you have any questions about how to use Autometa you can find the documentation at autometa dot readthedocs dot org, and if you are having trouble running it, you can submit an issue at our Github repository, where you can also download the source code.

```
Those links move up and then we show the NSF logo and the grant number
```

We also gratefully acknowledge NSF for funding the development of Autometa, under DBI grant number 1845890.




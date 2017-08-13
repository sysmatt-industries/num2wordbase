#!/usr/bin/perl 

my @lengths=split(",",$ARGV[0]);
foreach my $word (<STDIN>){
	$word =~ s/\s+.*//;
	chomp($word);
	#next if $word =~ m/\./;
	#next if $word =~ m/\-/;
	next unless $word =~ m/[aeiou]/i;  # Must has some vowel movement
	#/next if $word =~ m/[xyzvwk]/i;  # letters we cant really deal with
	#next if $word =~ m/[aeiou][aeiou]/i;  # double vowel
	next if $word =~ m/[aeiou][aeiou][aeiou]/i;  # nix tripple vowel 
	foreach my $length (@lengths){
		if ( length($word) == $length ){
			print "${word}\n";
			last;
		}
	}
}





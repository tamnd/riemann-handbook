---
title: The pair theorem and the closing of membership
decls:
  - GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt
  - GlobalTheory.Mem.Top.Closing.memberE_closing_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The pair theorem and the closing of membership

This section proves the membership statement and the bundle statement for the parameter set of a norm choice extension $N$, given a second extension $N_g$ that refines $N$ and a list of step conditions for both. This is the pair theorem. It is the last step of [the Theorem on the origin extension](/entry/exists-base-lattice-of-prime-alt/) of Section 1, which applies it to the origin extension and the geometric extension. The pair theorem joins three results: the export of built cores (Section 4), the closing theorem below for the membership statement, and the bundle statement for parameter sets of extensions with law, which a later section proves. We use the words of Section 1: the parameter set $p(N)$, its scale $s(N)$, the slots $Q_s$ and $Q'_s$ of built and good cores, the column step $\mathrm{Step}_w$, the start condition, $\mathrm{Has}_3$ and $\mathrm{Has}_4$, the pass condition and the bundle linkage $\Lambda_N$.

The closing theorem needs three statements on discrete series of the real unitary groups, which we write out. For $n \ge 1$ and a signature $\varepsilon \in \{0, 1\}^n$, let $U_\varepsilon$ be the unitary group of the diagonal hermitian form of signature $\varepsilon$, as a set of complex $n \times n$ matrices. A *Harish-Chandra parameter* is a strictly decreasing $\lambda \in \mathbb{R}^n$ with $\lambda_a - \frac{n-1}{2} \in \mathbb{Z}$ for all $a$. For a Hilbert space $H$ and a map $\sigma$ from complex $n \times n$ matrices to bounded operators on $H$, we say that $\sigma$ is a *discrete series with parameter* $\lambda$ for $\varepsilon$ if on $U_\varepsilon$ it is an irreducible, square integrable, unitary representation, with a $K$-type at the lowest $K$-type of $(\varepsilon, \lambda)$ that is minimal for the norm of $K$-types. See [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees).

**Theorem 6.2.1 (Discrete series of $U(p, q)$).** We take as given, from Harish-Chandra's classification of discrete series: (a) for each $n$, $\varepsilon$ and Harish-Chandra parameter $\lambda$ there are a complex Hilbert space $H$ and a discrete series $\sigma$ on $H$ with parameter $\lambda$ for $\varepsilon$; (b) two discrete series $\sigma, \sigma'$ on $H, H'$ with the same $\varepsilon$ and $\lambda$ are unitarily equivalent on $U_\varepsilon$: there is a linear isometry $U : H \to H'$ with $U(\sigma(g)v) = \sigma'(g)(Uv)$ for all $g \in U_\varepsilon$ and $v \in H$; (c) for each group datum of signature $(p, q)$ and each parameter $\lambda$ with rational entries that is admissible, there is a discrete series datum of the group datum with parameter $\lambda$.

These three statements are hypotheses of the closing theorem. They are not proved in this volume.

**Theorem 6.2.2 (Closing of membership).** Assume the following statements, which we take as given from the literature: the existence of ray class fields, the principal ideal statement, CM curves with good reduction outside a prime, the infinitesimal characters of discrete series, the finiteness theorem of Harish-Chandra, rapid decay of cusp forms (twice), uniqueness of discrete series of $U(p,q)$, finite dimension of the rows, convergence of the Siegel-Weil integral for unitary groups, existence of discrete series, a formal degree formula, the Siegel mass ratio for CM fields, the Weil representation of a unitary dual pair, the Casselman-Wallach theorem, the theory of Harish-Chandra modules, and the three statements (a), (b), (c) above. Let $h_L$ be a recursion datum and let $N, N_g$ be norm choice extensions for $h_L$. Write $s = s(N)$ and $s_g = s(N_g)$. Assume:

1. $\mathrm{Step}_w(\text{start}, \mathrm{Has}_3(s))$;
2. the level three condition for $s$ and for $s_g$;
3. the export condition for $Q_s$: at large bases eventually, with $\mathrm{KP}_x$ and untwisted $T$, every core in $Q_s$ exports;
4. the pass condition $\mathrm{Pass}(\mathrm{KP}_x, Q_s, r)$, where $r$ holds at a point if it has a column datum $w$ with the start condition and $\mathrm{Has}_3(s_g)$ at $w$;
5. each datum of $N_g$ at a point gives a datum of $N$ at the same point, and the good orientation condition holds there.

Then the membership statement holds for $s$.

Lean: `GlobalTheory.Mem.Top.Closing.memberE_closing_alt_alt`.

*Proof.* This is [the Theorem on construction steps](/entry/exists-member-of-construction-steps-second-pass/) applied to the two scales $s$ and $s_g$, with the first three statements of the list and the Siegel mass ratio. For each of the two scales we supply four inputs.

1. The column step from pinned columns of level three to level four, $\mathrm{Step}_w(\text{pinned} \wedge \mathrm{Has}_3, \mathrm{Has}_4)$. It is [the Theorem from level three to level four](/entry/has4-of-has3-of-lv3-mv/) of Section 3, applied with nine statements of the list and the level three condition of hypothesis 2. Its $S$-extension is trivial, as it is for every $p(N)$.
2. The ambient existence statement. It holds because the position of both scales is $\mathrm{RX}$.
3. The division existence statement. It follows from ray class fields, principal ideals and CM curves, because the geometric predicate of both scales is the closure of the trivial geometry.
4. The theta existence statement: theta data with true rows and columns that are compatible at all places. It follows from the Weil representation, rapid decay, the Casselman-Wallach theorem, Harish-Chandra modules and the three discrete series statements. Its side condition holds because the relevant index is $0$.

Hypotheses 1, 3 and 4 are passed on unchanged. The last input says that a core that is built for $s_g$ is good for $s$ and has all twists admissible. It follows from hypothesis 5: the datum of $N_g$ gives a datum of $N$, so the core is built for $s$, and the good orientation condition makes it good. $\square$

**Theorem 6.2.3 (Pair theorem).** Assume the records $\mathcal{H}_A$, $\mathcal{H}_E$ and $\mathcal{H}_M$ of Section 1. Let $h_L$ be a recursion datum with the record $\mathcal{H}_L(h_L)$, and let $N, N_g$ be norm choice extensions for $h_L$. Write $s = s(N)$ and $s_g = s(N_g)$. Assume:

1. each datum of $N$ at a point gives a datum of the extension with law at that point;
2. each datum of $N_g$ gives a datum of $N$ at which the good orientation condition holds;
3. $\mathrm{Step}_w(\text{start}, \mathrm{Has}_3(s))$;
4. the level three condition for $s$ and for $s_g$;
5. the moving condition for $s$: a witness at a stage $Z$ moves under each division of $Z$ to rows at which the four slots are nonempty;
6. the pass condition $\mathrm{Pass}(\mathrm{KP}_x, Q_s, r)$ with $r$ as in hypothesis 4 of the closing theorem;
7. the multiplicity condition for $p(N)$.

Then the membership statement holds for $s$, and the bundle statement $\mathrm{ExB}(\mathrm{KP}_x, Q_s, Q'_s, \Lambda_N)$ holds.

Lean: `GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt`.

*Proof.* There are three steps.

1. [The export theorem](/entry/automorphy-of-hypotheses-alt-alt/) of Section 4 gives the export condition for $Q_s$. It uses the twenty-five statements of $\mathcal{H}_E$, rapid decay of cusp forms and global Artin reciprocity from $\mathcal{H}_A$, three statements of $\mathcal{H}_L(h_L)$ (the published inputs of the third layer, the series input and the membership statement at layer points) and hypothesis 1.
2. The closing theorem above gives the membership statement for $s$. Its literature hypotheses are eighteen statements of $\mathcal{H}_A$, with rapid decay used twice. Its other hypotheses are hypotheses 3, 4, 6 and 2 and the export condition of step 1.
3. [The uniform theorem for geometric parameters](/entry/geometric-parameter-uniform-alt/) gives the bundle statement. It uses the discrete series cover and one theta condition statement of $\mathcal{H}_M$, nine statements of $\mathcal{H}_A$, hypothesis 1, the moving condition of hypothesis 5 and the multiplicity condition of hypothesis 7.

The two conclusions are those of steps 2 and 3. $\square$

So the pair theorem reduces the two statements for $p(N)$ to the export condition, the level three to level four step and the bundle statement. Sections 3 and 4 prove the first two. The rest of the chapter treats the inputs of the origin extension that feed the hypotheses of the pair theorem.

**Remark 6.2.4 (Formalization).** The theorems are at [ExistsBaseLatticeOfPrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L36) and [MemberEClosing.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberEClosing.lean#L17). In the pair theorem the hypothesis of type `PositionMv` has the local name `intersection_update_fsHerm_neg_one` (line 42), which has no relation to its type. The closing theorem takes `CuspRapidDecay` as two separate hypotheses, the sixth and the fourteenth, and the pair theorem passes the same field `a6` of `HypAAlt` to both (line 53). The local names of the hypotheses of the closing theorem skip `s7`. The field `par` of `LocalLanglandsHypothesis` is not used. The bundle half of the pair theorem is not used by the only chain of callers, because Section 1 proves the bundle statement for $N_0 \times A$ with another lemma. The names "base lattice" and "of pair" match no object of the statement. We have not checked that the three discrete series statements are faithful forms of the results of Harish-Chandra; they are hypotheses, and we did not unfold `IsDS`, `UJset`, `lowK`, `DSRep`, `IsParam`, `GoodO`, `LevelThreeCondition` beyond the sentence above, `ExportAt` or the theta existence statement `ThEx`. The step inputs are `has4_of_has3_of_lv3Mv` (twice), `ambEx_of_rx`, `divEx_geoCl`, `exists_thetaData_trueRowsColumns_allCompatible` with `io_zero`, and `goodE_of_builtE_alt`.

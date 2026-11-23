---
title: Joints at every tuple
decls:
  - GlobalTheory.T.jointsAtSplitUnramifiedPlaces_of_chainCharts
  - GlobalTheory.TwU.AllTuples.joints_all_true
  - GlobalTheory.T.trueColumn_joints_hold_all_tuples
  - GlobalTheory.Pdv.oneTie_jointsAt_all
  - GlobalTheory.T.kernel_relation_true_columns_joints_all_tuples
  - GlobalTheory.Svd.jointsAt_all_std
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Joints at every tuple

This section proves that a tied kernel entry has a *joint* at every tuple and at every place that avoids the primes of the tuple. A joint is the package of global data that connects a local formal group system at a place to the global kernel entry. The main result, Theorem 4, starts from an object that has a part over a column, and gives a kernel entry with joints at every tuple. Section 5 turns these joints into local models, and Section 6 uses the local models in [the service row](/entry/serv-h-row/).

### Joints and joint inputs

We fix the following setting for the whole chapter. Let $D$ be a datum of the development. It carries a CM field $E$ with maximal totally real subfield $F$, a field $K$ of complex multiplication, and a chain of Hermitian spaces over $E$ of ranks $N(0), N(1), \dots, N(m)$. We write $\mathcal{O}_E$ for the ring of integers of $E$ and $U^1(\mathbb{A}_f)$ for the group of finite ideles $x$ of $E$ with $x \bar{x} = 1$. A word $u$ and a tuple $\mu$ select the rows and the columns of the twisted chain of $D$. For a tuple $\mu$ we write $Q_p(\mu)$ for the finite set of primes that the tuple excludes. A place $w$ of the development has a residue characteristic $p$, and an index condition for $(u, w)$ says that $p$ is admissible for the word $u$.

Let $\mathrm{ex}$ be extra data over $D$. It contains a twist $\tau$ with step maps $e_0$ and $e_{\mu_0}$, and a comparison map. A *tied kernel entry* $t$ for $\mathrm{ex}$ carries an ideal $\mathfrak{c}$ of $\mathcal{O}_K$, a complex number $\delta$, a base $B$ of lattice data, a character $\chi$, an embedding $\sigma_0$ of the field of the entry into $\mathbb{C}$, and for each pair $(u, \mu)$ a record with a level $\ell$, a family of series $\Xi$, a finite set $S$ of bad primes, characters $\mathrm{mt}_j$ and a determinant map $\mathrm{dt}$.

**Definition 5.1.1 (Joint).** Let $t$ be a tied kernel entry for $\mathrm{ex}$. Fix a word $u$, a tuple $\mu$, a place $w$ of residue characteristic $p$ with its index condition, levels $L_v$ at $w$, and comparison inputs $I$, hypotheses $H$ and labels $X$ over these levels. A *joint* for $t$ at these data consists of the following.
1. Group compatibility data for the comparison map, chain charts $S_t$ for $(u, \mu)$, and an adelic datum $A$ on these charts.
2. A homomorphism $\mathrm{dt}_U$ from $U^1(\mathbb{A}_f)$ to the determinant group of $D$, an element $a \in \mathcal{O}_E$, and the pins and the tie of $(A, \mathrm{dt}_U, a)$.
3. Identifications at step $0$: a bijection of the classes at step $0$ of the member and of the twist, a bijection of the points at step $0$, and the equality of the frames, levels and characters at step $0$.
4. A sharp form at every level and every lattice vector.
5. The lattice tie of the extra data, the condition $p \notin Q_p(\mu)$, and the condition that the norm of $\mathfrak{c}$ is prime to $p$.
6. Algebraicity: every value of $\sigma_0$ lies in the image of a fixed number field $L$ in $\mathbb{C}$, and the same holds at step $0$.

**Definition 5.1.2 (Joints at a tuple).** The entry $t$ *has joints at* $\mu$ if for every word $u$, every place $w$ with its index condition, and $p \notin Q_p(\mu)$, there are levels $L_v$, inputs $I$, hypotheses $H$ and labels $X$ with a joint for $t$ at these data.

A joint is built from a smaller set of data, which we call joint inputs.

**Definition 5.1.3 (Joint inputs).** Let $t$ be a tied kernel entry, $u$ a word and $\mu$ a tuple. *Joint inputs* for $(t, u, \mu)$ consist of group compatibility data, symmetric Hermitian columns with their relative determinant, chain charts $S_t$, an adelic datum $A$ on them, an element $a \in \mathcal{O}_E$ with pins and a tie, valuation data for the twist on $S_t$, and the following facts:
1. at each step the set of chart classes is finite;
2. each level character has finite order;
3. the base lattice of each chart class, read in the coordinates of $A$, is the standard lattice;
4. the joint conditions and the identifications at step $0$;
5. the rationality of the twist at every step $j < m$;
6. the values of $\sigma_0$ lie in the image of $L$.

**Theorem 5.1.4 (Joints from joint inputs).** Let $t$ be a tied kernel entry for $\mathrm{ex}$ and $\mu$ a tuple. Assume the lattice tie of the extra data, and assume that for every word $u$ there are joint inputs for $(t, u, \mu)$. Then $t$ has joints at $\mu$.

Lean: `GlobalTheory.T.jointsAtSplitUnramifiedPlaces_of_chainCharts`

*Proof.* This is [the theorem on joints from joint inputs](/entry/joints-at-of-j-in/) of a later section, applied to the same data. $\square$

### True columns

The joint inputs come from a true-column datum. A *true-column datum* $I$ fixes a family of laws $l$, a law $l_0$ at step $0$, and for each later stage $Z$ a datum $D(l, Z)$ with a set of tuples $\iota$. We work over the datum $D = D(l, Z)$. The datum $I$ has its own twist $\tau_I(l, l_0, Z)$, its own error part, and its own standard objects: a standard kernel, standard reads, standard columns, standard level forms and a standard determinant.

**Theorem 5.1.5 (Joints over true columns).** Let $I$ be a true-column datum that is in order and has pins. Fix laws $l$, a law $l_0$ at step $0$, a later stage $Z$, extra data $\mathrm{ex}$ over $D = D(l, Z)$, a tied kernel entry $t$ for $\mathrm{ex}$, symmetric tied columns $C$ that are full, and Hermitian data $g$. Assume the following.
1. The twist of $\mathrm{ex}$ is $\tau_I(l, l_0, Z)$, and the error part of $\mathrm{ex}$ is the error part of the base.
2. $I$ is a twisted datum and its jets are in place.
3. $t$ is the standard kernel and has the standard reads at $(l, Z)$.
4. For each word $u$, tuple $a$, step $i$ and class $c$ at step $i$, the entry pins $(i, c)$ if and only if $i + 1 \le m$ or the representative of $c$ lies over a row of the selection.
5. $C$ is standard, the determinant of the full columns is standard, the Hermitian form of $g$ is the form of the full columns, and the forms of $g$ are the forms of $C$.
6. Every value of the character $\chi_D$ of $D$ lies in the image of $L$.
7. The lattice tie of the extra data holds.

Then $t$ has joints at every tuple $a \in \iota$, and for every word $u$ the step maps of the twist satisfy $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$.

Lean: `GlobalTheory.TwU.AllTuples.joints_all_true` (also `GlobalTheory.T.trueColumn_joints_hold_all_tuples`)

*Proof.* Fix a tuple $a$. For every word $u$, [the existence of chain charts over true columns](/entry/true-column-exists-chain-charts-kernel-data-forms/) gives joint inputs for $(t, u, a)$ from the hypotheses. The theorem on joints from joint inputs then gives joints at $a$. For the second claim, fix a word $u$. By hypothesis 1 the twist is $\tau_I(l, l_0, Z)$. For this twist the identity $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ is a lemma on the step maps of the twist of a true-column datum. $\square$

The next result drops hypotheses 3 and 4 on the reads and the pins. The price is that the conclusion is about a different kernel entry.

**Theorem 5.1.6 (Joints from a standard kernel).** Let $I$, $l$, $l_0$, $Z$, $\mathrm{ex}$, $t$, $C$ and $g$ be as in the previous theorem, together with a tied tuple $\mathrm{tp}$ whose series is the series of $I$. Assume hypotheses 1, 2, 5, 6 and 7 of the previous theorem. Assume that $t$ is the standard kernel at $(l, Z)$, and that the level forms of $C$ are standard. Then there is a tied kernel entry $t'$ for $\mathrm{ex}$ that has joints at every tuple. Also $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$.

Lean: `GlobalTheory.Pdv.oneTie_jointsAt_all` (also `GlobalTheory.T.kernel_relation_true_columns_joints_all_tuples`)

*Proof.* A marking lemma for standard kernels takes the standard kernel $t$ and gives a tied kernel entry $t'$. The entry $t'$ is again the standard kernel, it has the standard reads, and it satisfies the pin condition 4 of the previous theorem. We apply the previous theorem to $t'$. It gives joints of $t'$ at every tuple and the identity of the step maps. $\square$

### Objects with a part

The last step starts from an object over a column. Let $B$ be a base, $f$ a frame of the base and $T$ twist data. A *column* $w$ over $(B, f, T)$ has a true-column datum, laws $l$ and $l_0$, and pins. For each later stage $Z$ of $w$ we have the datum $D(w, Z)$. An *object* $O$ over $D(w, Z)$ bundles size data, a lattice tie, Hermitian data, constants, divisor data and extra data $\mathrm{ex}(O)$. A *part* of $O$ over $(w, Z)$ consists of pins, a column record (tied columns $C$, their fullness, Hermitian data $g$ and the standard facts), an error part, a tied tuple, a series, a set of primes, and a kernel record that equals the extra data of $O$. Its kernel tie gives the equality of the twist with the twist of the column, the error part, a tied kernel entry $t$, and the fact that $t$ is the standard kernel.

**Theorem 5.1.7 (Joints over an object with a part).** Let $w$ be a column over $(B, f, T)$, $Z$ a later stage, and $O$ an object over $D(w, Z)$. Assume that $O$ has a part over $(w, Z)$ and that the lattice tie of $O$ holds. Then there is a tied kernel entry $t$ for $\mathrm{ex}(O)$ that has joints at every tuple $\mu$. Also $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$.

Lean: `GlobalTheory.Svd.jointsAt_all_std`

*Proof.* The kernel tie of the part gives the twist equality, the error part, a kernel entry $t$ and the fact that $t$ is the standard kernel. A lemma on the values of $\chi_D$ over a column says that every value of $\chi_D$ lies in the image of $L$. The part also contains a kernel record and the equality of this record with the extra data of $O$. Both sides are dependent pairs. Equality of the first components identifies the size data, and equality of the second components identifies the constants. After these two substitutions the column record of the part provides $C$, its fullness, $g$, the standard facts, and the pins of the column. Now all hypotheses of the theorem on joints from a standard kernel hold, and that theorem gives the result. $\square$

**Remark 5.1.8 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.trueColumn_joints_hold_all_tuples` and `GlobalTheory.T.kernel_relation_true_columns_joints_all_tuples` are second names. Each is proved by the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` under `maxHeartbeats 1000000`.
2. The theorem `GlobalTheory.T.jointsAtSplitUnramifiedPlaces_of_chainCharts` is also only a second name. Its proof is `GlobalTheory.TwV.jointsAt_of_jIn`, which a later section treats. In the code the joint inputs are the structure `JIn` (JointCmpEmbeddingYAlt.lean:54), and the joint is the structure `Joint` with 35 fields (JointCmpEmbeddingY.lean:35). The name says "split unramified places", but the only condition on the place in `JointsAt` is that the residue characteristic is not in `Dx.Qp μ`.
3. In `GlobalTheory.Pdv.oneTie_jointsAt_all` the hypotheses `_htp` (the series of the tuple equals the series of the datum) and `_hLv` (the level forms are standard) are not used (KernelRelationTrueColumnsJointsAllTuples.lean:16). The conclusion is about a new entry $t'$, which comes from `GlobalTheory.Pdv.stdKer_stdRd_mark`, and not about the given $t$. The words "kernel relation" in the second name do not match the statement.
4. In `GlobalTheory.Svd.jointsAt_all_std` four of the eight facts of `Part.kerTie` are discarded with `-` (JointsAtAllStd.lean:13). The proof unpacks the object and the part, and uses `congrArg Sigma.fst` and `eq_of_heq` on the field `ker_eq` to substitute the size data and the constants.
5. The second claim of each theorem is the hypothesis on the twist that Section 5 needs for local models.

---
title: Twisted chains on true columns
decls:
  - GlobalTheory.Mem.Col2.TwistLevel.exists_levJ_cosets
  - GlobalTheory.T.exists_penultimateLevel_couplingCosets
  - GlobalTheory.Mem.Col2.TC.twPack_ex
  - GlobalTheory.Mem.Col2.TC.tw_chains
  - GlobalTheory.T.trueColumnChoice_twistedChains_formsClasses
  - GlobalTheory.Mem.Col2.TC.tw_ties_with_points
  - GlobalTheory.T.trueColumnChoice_exists_chainData_with_basePoints
  - GlobalTheory.Mem.Col2.TC.colsTwPTiedS_std
  - GlobalTheory.T.trueColumnChoice_exists_standardChainData
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Twisted chains on true columns

A true column choice gives, for each word $u$ and each twist index $a$, a chain of steps $0, 1, \dots, m$ with classes of lattice points and their stabilizers. The kernels of the columns are read off from level charts on these steps, and the chart at step $m - 1$ must be coupled to the level $J$ of the forms. In this section we build these charts, which we call twisted chains, and we add the base points at the top step and the level structure. The result is a standard chain datum for each true column choice. It enters [the nonempty hypotheses at unramified exponents](/entry/hypotheses-nonempty-of-unramified-exponents-alt/).

### The setting

Let $B$ be a base, $X$ a pre-datum and $I$ a true column choice over $B$ and $X$, good and with the pins of the true columns. Let $l$ be the laws of $I$, $Z$ a later stage of its columns, and $D = D(I, l, Z)$ the ambient datum of the stage. For a word $u$ the host gives the type prime $T_u$, and for an index $a$ the twisting character $\xi_a$. A place $v$ of $F$ is under $Q$ for $a$ if some place $w$ of $E$ over $v$ is ramified for $\xi_a$. Let $Q_a$ be the finite set of these places. The reference index is $\mu_0$, and $\xi_{\mu_0}$ is unramified everywhere.

Let $H$ be hermitian column characters for $D$: for each word $u$ and step $i$ a set of characters $\mathrm{Ch}(u, i)$ with a map from the classes of the column. Let $F$ be a family of forms tied to $H$, one for each word. The forms $F(u)$ have a level $J$, the level of step $m - 1$, with a group $U_J$ and a character $\chi_J$, and levels at the other steps. We say that $F$ is standard if each $F(u)$ satisfies the standard conditions of the forms, and that its levels are standard if in addition the level $J$ has the standard frame values $1$ at each step and place. The datum $H$ has characters on the hermitian forms if the class maps of $H$ and $F$ agree with the characters of $D$ at step $0$, at the columns and at the base.

**Definition 1.20.1 (Twisted step).** Let $u$ be a word, $a$ an index, $i$ a step and $Q$ a set of places. A twisted step consists of a finite set $C_i$ of chart labels with a map from the classes of step $i$ of the chain of $(u, a)$ and a map to $\mathrm{Ch}(u, i)$, and, for $1 \le i \le m$ and each label $\beta$, a level chart $K(\beta)$ on the classes with label $\beta$ at the places off $Q$ and the type primes. Each chart has a group $U$, a character $\chi$ and a lattice $L_b$. The step must read the kernels of the chain through the charts. When $i + 1 \le m$, there are elements $k_\beta$ of the adelic group of rank $N_i$ with trivial components at the places under $Q$, through which the classes are read. The charts kill the function of the type prime of $u$, and their characters have finite order off $Q$.

At the top step $m$ the step has three more properties: the character of each chart agrees with the character of the forms on elements that are trivial at $Q$; for $a \ne \mu_0$ the chart groups are the top base groups; and for $a \ne \mu_0$ there are elements $k_\beta$ that read the top classes and move base points. The last property says: if $g'$ in the group of rank $N_m - 1$ is a point for a datum $d$, and $g$ is an extension of $g'$ at the base point $z_0(u)$, then $g k_\beta$ is a point for the moved datum $\tilde{F}(d)$.

### The level at step m minus 1

**Definition 1.20.2 (Coupling cosets).** Let $u$, $a$, $Q$ be as above, and let a twisted step at $m - 1$ be given, with labels $C$ and charts $K(\beta)$. A coupling datum consists of a level $J'$ at step $m - 1$, a finite set $Y_b$ with an action of its group $U_{J'}$, a point $y_b(\beta)$ for each label with one orbit for each label, and a character $\chi_{J'}$. Each chart lattice and chart group lies in $J'$. An element $\kappa$ of $U_{J'}$ fixes $y_b(\beta)$ if and only if its image lies in the group of $K(\beta)$. The character $\chi_{J'}$ restricts to the character of each chart, and the conditions of $J$ hold at the primes $g_i$.

**Theorem 1.20.3 (Coupling cosets at step m minus 1).** Let $I$ be good with its pins, $F$ standard with levels of frame value $1$ at the level $J$, and $Q = Q_a$. Let a twisted step at $m - 1$ be given, with its readings, with characters of finite order, with charts trivial off the places of $Q$ in the sense of the step, and with characters compatible along the steps. Then a coupling datum exists.

Lean: `GlobalTheory.Mem.Col2.TwistLevel.exists_levJ_cosets` (also `GlobalTheory.T.exists_penultimateLevel_couplingCosets`, a second name).

*Proof.* The group of the further places contains the levels of all charts. This step uses that the characters have finite order. With this group, the coupling datum exists by the construction from the further places. $\square$

**Definition 1.20.4 (Twisted package).** A twisted package for $(u, a)$ is a twisted step at each $i$, with the top properties at $m$, a coupling datum at $m - 1$, and the condition that $\chi_{J'}(\kappa) = \chi_J(\kappa')$ whenever $\kappa'$ is the image of $\kappa$ and $\kappa$ is trivial at each place of $Q$.

**Theorem 1.20.5 (Twisted packages).** Let $I$ be good with its pins, $u$ a word and $a$ an index, $Q$ the set $Q_a$, $F$ standard, with frame values $1$ at the level $J$, and assume that $H$ has characters on the hermitian forms. Then a twisted package for $(u, a)$ exists.

Lean: `GlobalTheory.Mem.Col2.TC.twPack_ex`.

*Proof.* Step 1 (the steps). At step $0$ and at the steps above $m$ the twisted step is the trivial one, with the labels given by the class maps. At a middle step $1 \le i \le m - 1$ it comes from the middle construction, and at step $m$ from the top construction, which also gives the top properties. Step 2 (finite order). For $a = \mu_0$ the characters of the charts at $m - 1$ are trivial on elements trivial at the type places, since no place is a twist place of the reference tuple; so they have order $1$. For $a \ne \mu_0$ the step gives the finite order. Step 3 (coupling). The theorem on coupling cosets gives a coupling datum $J'$ at $m - 1$. Step 4 (the character). The class set at step $m - 1$ is not empty, since the last index of the character index has one element and gives the base class. With a class $c$, the lattice of $J$ is the image of the lattice of $J'$, because both are the lattice of the chart of $c$. The character of the level $J$ off the places then gives a character $\chi$ of $U_{J'}$ that restricts to each chart character and agrees with $\chi_J$ on elements trivial at $Q$. Replacing $\chi_{J'}$ by $\chi$ gives the package. $\square$

### Twisted chains and base points

**Theorem 1.20.6 (Twisted chains on true columns).** Let $I$ be good with its pins, $l$ its laws, $Z$ a later stage and $l_0$ the law at step $0$. Let $\mathrm{in}Q(a, v)$ be a relation with $\mathrm{in}Q(a, v)$ if and only if $v$ is under $Q$ for $a$. Let $H$ and $F$ be as above, with $F$ standard and with standard levels, and $H$ with characters on the hermitian forms. Assume that the level $J$ of each $F(u)$ has frame value $1$ at each step and place. Then there are chains $T$, coupling data $J$ and twisted forms $W$ for all $(u, a)$ such that: the chains agree with the chain of $I$ on the classes and with the class map of $\mu_0$ at step $0$; the forms at the type places are the restrictions of $F$; each step reads its kernels; the top groups are the top base groups; the top base points move as in the top properties; the charts kill the functions of the type primes; and the coupling data are compatible.

Lean: `GlobalTheory.Mem.Col2.TC.tw_chains` (also `GlobalTheory.T.trueColumnChoice_twistedChains_formsClasses`, a second name).

*Proof.* For each $a$ let $Q_a$ be the image of the primes of $I$ for $a$ under the map $P \mapsto P \cap \mathcal{O}_F$. Then $v \in Q_a$ if and only if $v$ is under $Q$ for $a$, which is $\mathrm{in}Q(a, v)$. For each $(u, a)$ the theorem on twisted packages gives a package $p(u, a)$. The forms at the type places exist for each $(u, a)$. The places of $Q_a$ are prime to $T_u$ and to the primes $g_j$. The chains, the coupling data and the forms are now read from the packages. The restriction property holds because the forms $F(u)$ are standard. The other properties are the properties of the steps and of the top. $\square$

**Corollary 1.20.7 (Twisted chains with base points).** In the setting of the previous theorem, but without the assumption on the frame values of $J$, there are $T$, $J$ and $W$ with the same properties, and in addition for $1 \le m$, each word $u$ and each $a \ne \mu_0$ there are elements $k_\beta$ that read the top classes and send each point $g$ that extends a point $g'$ for $d$ to the point $g k_\beta$ for $\tilde{F}(d)$.

Lean: `GlobalTheory.Mem.Col2.TC.tw_ties_with_points` (also `GlobalTheory.T.trueColumnChoice_exists_chainData_with_basePoints`, a second name).

*Proof.* The standard levels of $F(u)$ give the frame values $1$ at $J$. So the theorem on twisted chains applies. The additional claim is the top base point property of the packages. $\square$

### Standard chain data

A tied tuple $t_p$ for the ambient datum $D$ is a tuple of characters $\xi$ with a choice $n$ and the places $\mathrm{In}Q'(a, v)$ of its twist. Symmetric tied columns $C$ consist of hermitian column characters, forms $F(u)$ tied to them, and the characters of $D$ at step $0$, at the columns and at the base.

**Theorem 1.20.8 (Standard chain data).** Let $I$ be good with its pins, $l$ its laws, $Z$ a later stage, $l_0$ the law at step $0$, $n$ a choice, $t_p$ a tied tuple and $C$ symmetric tied columns. Assume that the characters of $t_p$ are the characters $\xi$ of $I$, that the forms of $C$ are standard, and that their levels are standard. Then there are symmetric twisted columns at the primes, with chains, coupling data, forms, a level structure and points, that are standard.

Lean: `GlobalTheory.Mem.Col2.TC.colsTwPTiedS_std` (also `GlobalTheory.T.trueColumnChoice_exists_standardChainData`, a second name).

*Proof.* Step 1. For each $a$ and $v$, $v$ is in the twist set of $t_p$ if and only if $v$ is under $Q$ for $a$: both say that $\xi_a$ is ramified at a place over $v$, since $\xi_a$ is read by its tuple. Step 2. The symmetric columns give characters on the hermitian forms. Step 3. The corollary on twisted chains with base points gives $T$, $J$ and $W$. Step 4. The tuple chains have a level structure at the level prime, compatible with $T$, $J$ and $W$, and the level data agree. Step 5. The layers of the tuples are compatible at the prime $X$, which gives the points and their properties. These data are the standard twisted columns. $\square$

**Remark 1.20.9 (Formalization).** In [TrueColumnChoiceTwistedChainsFormsClasses.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TrueColumnChoiceTwistedChainsFormsClasses.lean#L464) the theorem `tw_chains` takes the hypothesis that $F$ is standard with standard levels, but uses only the first half, and it takes the frame values of $J$ as a separate hypothesis. That hypothesis follows from the standard levels, as `tw_chains_std` at line 488 shows, so it is redundant. In the proof of `twPack_ex` (line 272) the step at line 317 is `first | exact hoffx hLb | exact hoffx`, a hedge between two forms of the same lemma. The coupling datum is `TwLevJ` ([ChartWiden.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ChartWiden.lean#L46)). The conditions `StdF`, `StdLvC`, `CarH`, the middle and top step constructions and the lemmas of Steps 4 and 5 of the last proof are not unfolded here; we state them as they are used.

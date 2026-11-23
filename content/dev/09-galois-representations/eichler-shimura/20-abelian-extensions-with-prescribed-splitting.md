---
title: Abelian CM extensions with prescribed splitting
decls:
  - UpperTheory.Gal.UnramifiedFromSplittingCriterion.unrSplit_holds
  - UpperTheory.Gal.UnramifiedFromSplittingCriterion.unrField_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Abelian CM extensions with prescribed splitting

The toral step of Section 17 ([Theorem 3.17.11](/entry/to-tor-holds/)) moves a cuspidal representation from a CM field $E$ to an abelian CM extension $K/E$, one cyclic layer of prime degree at a time. It needs a field $K$ with three properties: $K/E$ is unramified above a given split place $w$, the places of $K$ above $w$ have a prescribed residue degree $f$, and $K/E$ is unramified at every place that does not split over $E^+$. It also needs control of the new ramification in each layer. This section constructs such a field. The construction is class field theory over $E^+$: we choose a character of $G_{E^+}$ with the right Frobenius order at $w$, and then we correct it by characters ramified at fresh split places, so that its kernel is reached by prime steps.

### Notation

Let $E$ be a CM field with maximal totally real subfield $E^+$, and let $\Omega$ be an algebraic closure of $E$. For a field $F \subseteq \Omega$ write $G_F = \mathrm{Gal}(\Omega/F)$. A place of $\Omega$ is a valuation ring $A$ of $\Omega$. For a finite place $v$ of a number field $F \subseteq \Omega$, we say that $A$ lies over $v$ if an integer $x$ of $F$ has $|x|_A < 1$ exactly when $x \in v$. Then $D_A(F) \subseteq G_F$ is the decomposition group (the $\sigma$ with $\sigma A = A$) and $I_A(F) \subseteq D_A(F)$ is the inertia group (the $\sigma \in D_A(F)$ with $|\sigma x - x|_A < 1$ for all $x \in A$). Let $N(v) = |\mathcal{O}_F/v|$. An element $\varphi \in G_F$ is a *Frobenius at $A$ for $q$* if $\varphi \in D_A(F)$ and $|\varphi x - x^q|_A < 1$ for all $x \in A$. A finite place $w$ of $E$ is *split over $E^+$* if some place $w' \neq w$ of $E$ has the same restriction to $E^+$. An element $g \in G_F$ *fixes* a subfield $K \subseteq \Omega$ if $g(x) = x$ for all $x \in K$.

**Definition 3.21.1 (Good subgroup).** A subgroup $H \subseteq G_{E^+}$ is *good* if it is open, it contains the commutator subgroup of $G_{E^+}$, and it contains every complex conjugation: every $c \in G_{E^+}$ such that $j \circ c = \overline{j}$ for some embedding $j : \Omega \to \mathbb{C}$. It is *ramified only at split places* if for every finite place $t$ of $E^+$ and every $A$ over $t$, either $I_A(E^+) \subseteq H$ or $D_A(E^+)$ fixes $E$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.Good` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.RamSplit`).

The fixed field of a good subgroup is a finite abelian extension of $E^+$ in which every complex conjugation acts trivially, so it is totally real. Its compositum with $E$ is then an abelian CM extension of $E$. The second condition says that the fixed field ramifies only at places of $E^+$ that split in $E$: when $D_A(E^+)$ fixes $E$, the place under $A$ splits in $E/E^+$.

**Definition 3.21.2 (Abelian CM extension, layer, tower).** An *abelian CM extension of $E$ in $\Omega$* is a CM number field $K$ with $E \subseteq K \subseteq \Omega$ such that $K/E$ is Galois with abelian group. Such a $K$ *cuts out* a subgroup $H \subseteq G_{E^+}$ if an element $g \in G_E$ fixes $K$ exactly when $g \in H$. Let $S$ be a set of finite places of $E$. If $K \subseteq K'$ are two abelian CM extensions of $E$ in $\Omega$, then $K'$ is an *$S$-layer* over $K$ if $K'/K$ is Galois of prime degree and there is a finite place $u \notin S$ of $E$ such that:

1. for every $A$ over $u$, the group $D_A(E^+)$ fixes $E$ and $K$;
2. for some $A$ over $u$, some element of $I_A(K)$ does not fix $K'$.

An *$S$-tower* is a field $K$ with a chain $E = K_0 \subseteq K_1 \subseteq \dots \subseteq K_m = K$ in which each $K_{i+1}$ is an $S$-layer over $K_i$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.Fld` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.Cuts`, `UpperTheory.Gal.UnramifiedFromSplittingCriterion.Layer`, `UpperTheory.Gal.UnramifiedFromSplittingCriterion.Tower`).

Condition 1 says that $u$ splits over $E^+$ and that the place of $E^+$ under $u$ splits completely in $K$. Condition 2 says that $K'/K$ is ramified at the place of $K$ under $A$. So each layer is cyclic of prime degree, and its new ramification lies at a place outside $S$ that splits completely from $E^+$ to $K$. This is the form in which cyclic base change is applied, one layer at a time, in the proof of [Theorem 3.17.11](/entry/to-tor-holds/).

### The splitting criterion

**Theorem 3.21.3 (Abelian CM extensions with prescribed splitting).** Let $E$ be a CM field and $\Omega$ an algebraic closure of $E$. Let $w$ be a finite place of $E$ that is split over $E^+$, let $f \geq 1$ be an integer, and let $S$ be a finite set of finite places of $E$. Then there is an abelian CM extension $K$ of $E$ in $\Omega$ such that:

1. $K$ is an $S$-tower;
2. for every place $A$ of $\Omega$ over $w$, the group $I_A(E)$ fixes $K$, and every place $w'$ of $K$ under $A$ has $N(w') = N(w)^f$;
3. for every finite place $u$ of $E$ that is not split over $E^+$ and every $A$ over $u$, the group $I_A(E)$ fixes $K$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.unrSplit_holds` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.UnrSplit`).

The proof uses seven facts. We state them first.

**Lemma 3.21.4 (Characters with a given Frobenius order).** Let $v$ be a finite place of $E^+$ and $f \geq 1$. There is a continuous character $r : G_{E^+} \to \mathbb{C}^\times$ whose kernel is good and ramified only at split places, such that for every $A$ over $v$ we have $I_A(E^+) \subseteq \ker r$, and $r(\varphi)$ has order exactly $f$ for every Frobenius $\varphi$ at $A$ for $N(v)$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.unrCharAt_of` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.UnrCharAt`, `UpperTheory.Gal.UnramifiedFromSplittingCriterion.UnrCharPP`).

*Proof.* We take the case where $f$ is a prime power $\ell^k$ as given (see the Remark). For general $f$ use induction on the factorization. If $f = ab$ with $a, b$ coprime and characters $r_a$, $r_b$ exist, put $r = r_a r_b$. Then $\ker r \supseteq \ker r_a \cap \ker r_b$, and the two kernel conditions pass to intersections and to larger subgroups, so $\ker r$ is good and ramified only at split places, and $r$ kills $I_A(E^+)$. At a Frobenius $\varphi$ the values $r_a(\varphi)$ and $r_b(\varphi)$ have coprime orders $a$ and $b$, so $r(\varphi)$ has order $ab$. $\square$

**Lemma 3.21.5 (Fresh characters).** Let $U \subseteq G_{E^+}$ be an open subgroup, $T$ a finite set of finite places of $E^+$, and $n \geq 1$. There is a character $\psi$ of $G_{E^+}$ with $\psi^n = 1$, whose kernel is good and ramified only at split places, which is trivial on $D_A(E^+)$ for every $A$ over a place of $T$, and a finite place $u \notin T$ such that for every $A$ over $u$ we have $D_A(E^+) \subseteq U$ and some $\tau \in I_A(E^+)$ with $\psi(\tau)$ of order $n$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.FreshSplit` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.freshSplit`).

**Lemma 3.21.6 (Group step).** Let $\Gamma$ be a group with a class of *admissible* subgroups that is closed under finite intersections and under passage to larger subgroups. Let $P$ be a property of subgroups, $D \subseteq \Gamma$ a subset, and $(\mathrm{Dc}_u, \mathrm{I}_u)$ a family of pairs of subsets of $\Gamma$ with $\mathrm{I}_u \subseteq \mathrm{Dc}_u$. Assume:

1. for every admissible $U$ and $n \geq 1$ there are a character $\psi$ of $\Gamma$ with admissible kernel, $\psi^n = 1$ and $\psi = 1$ on $D$, and an index $u$ with $\mathrm{Dc}_u \subseteq U$ and some $\tau \in \mathrm{I}_u$ with $\psi(\tau)$ of order $n$;
2. if $H' \subseteq H$ are admissible, $P(H)$ holds, the index $[H : H']$ is prime, and some $u$ has $\mathrm{Dc}_u \subseteq H$ and $\mathrm{I}_u \not\subseteq H'$, then $P(H')$ holds.

Then for every admissible $H_0$ with $P(H_0)$ and every character $r$ of $\Gamma$ with admissible kernel and $r^n = 1$ for some $n \geq 1$, there is a character $r'$ with admissible kernel, $r' = r$ on $D$, and $P(H_0 \cap \ker r')$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.groupStep` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.GroupStep`).

The idea is that $r$ itself may have a kernel that is not reached by prime steps with fresh ramification. Hypothesis 1 supplies characters that are trivial on $D$ but ramified at new places, and multiplying $r$ by them does not change $r$ on $D$. The proof is finite group theory; we do not reproduce it.

**Lemma 3.21.7 (Fields from subgroups and layers).** (a) For every good $H \subseteq G_{E^+}$ there is an abelian CM extension of $E$ in $\Omega$ that cuts out $H$. (b) Let $H' \subseteq H$ be subgroups of $G_{E^+}$ with $H'$ good and $[H : H']$ prime, let $K$ and $K'$ cut out $H$ and $H'$, and let $u$ be a finite place of $E^+$ that is not under any place of $S$. Assume that for every $A$ over $u$, $D_A(E^+)$ fixes $E$ and lies in $H$, and that for some $A$ over $u$ some $\tau \in I_A(E^+)$ is not in $H'$. Then $K'$ is an $S$-layer over $K$, and $[K' : K] = [H : H']$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.ExFld` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.LayerOf`).

**Lemma 3.21.8 (Residue degree and splitting).** (a) Let $F \subseteq M \subseteq \Omega$ be number fields, $A$ a place of $\Omega$ over a place $v$ of $F$ and a place $w$ of $M$. Assume that $I_A(F)$ fixes $M$, that $\varphi$ is a Frobenius at $A$ for $N(v)$, and that for some $d \geq 1$ the power $\varphi^k$ fixes $M$ exactly when $d \mid k$. Then $N(w) = N(v)^d$. (b) Let $L$ be a CM field and $A$ a place of $\Omega$ over a place $w$ of $L$. Then $w$ is split over $L^+$ if and only if $D_A(L^+)$ fixes $L$.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.DegOf` (also `UpperTheory.Gal.UnramifiedFromSplittingCriterion.SplitIff`).

We use the last three lemmas without proof (see the Remark). Part (a) of the last one says that the residue degree of $w$ over $v$ is the order of Frobenius in $\mathrm{Gal}(M/F)$, when $w$ is unramified. Part (b) says that $w$ splits in $L/L^+$ exactly when its decomposition group lies in $G_L$.

*Proof of the Theorem.* Let $v$ be the restriction of $w$ to $E^+$. By the lemma on Frobenius orders there is a character $r$ of $G_{E^+}$ whose kernel is good and ramified only at split places, unramified at every $A$ over $v$, with $r(\varphi)$ of order $f$ at each Frobenius $\varphi$ over $v$. Since $\ker r$ is open, $r$ has finite order $m$. Let $T$ be $v$ together with the restrictions to $E^+$ of the places of $S$. This is a finite set.

Apply the group step to $\Gamma = G_{E^+}$, with these choices. A subgroup is admissible if it is good and ramified only at split places. $P(H)$ says that some $S$-tower cuts out $H$. $D$ is the union of the groups $D_A(E^+)$ for $A$ over $v$. The indices $u$ are the finite places of $E^+$ not under $S$ whose decomposition groups fix $E$, with $\mathrm{Dc}_u$ and $\mathrm{I}_u$ the unions of the decomposition and inertia groups over $u$. The two closure properties hold, since each defining condition passes to intersections and to larger subgroups. For hypothesis 1, take $U$ admissible and $n \geq 2$, and apply the lemma on fresh characters to $U$, $T$ and $n$. It gives $\psi$, trivial on $D$ because $v \in T$, and a place $u \notin T$, so $u$ is not under $S$. The place $u$ splits in $E$: some $\tau \in I_A(E^+)$ has $\psi(\tau) \neq 1$, so $I_A(E^+) \not\subseteq \ker \psi$, and since $\ker \psi$ is ramified only at split places, $D_A(E^+)$ fixes $E$. For $n = 1$ take the trivial character and the place given by the case $n = 2$. Hypothesis 2 follows from part (a) of the lemma on fields, which gives a field $K'$ that cuts out $H'$, and from part (b), which shows that $K'$ is an $S$-layer over the tower $K$ that cuts out $H$, so $K'$ is again an $S$-tower. Finally take $H_0 = G_{E^+}$, which $E$ cuts out, with the trivial tower.

The group step gives a character $r'$ whose kernel is good and ramified only at split places, with $r' = r$ on each $D_A(E^+)$ for $A$ over $v$, and an $S$-tower $K$ that cuts out $\ker r'$. Thus $g \in G_E$ fixes $K$ if and only if $r'(g) = 1$. This gives property 1. We check properties 2 and 3.

Let $A$ lie over $w$, so $A$ lies over $v$. Then $I_A(E) \subseteq I_A(E^+) \subseteq D_A(E^+)$. On this group $r' = r$, and $r$ kills $I_A(E^+)$. So $I_A(E)$ fixes $K$. For the norm, $w$ is split, so $D_A(E^+)$ fixes $E$ by part (b) of the last lemma. Part (a), applied to $E^+ \subseteq E$ with $d = 1$, gives $N(w) = N(v)$. Let $\varphi \in G_E$ be a Frobenius at $A$ for $N(w)$. It is also a Frobenius at $A$ for $N(v)$ in $G_{E^+}$. Since $\varphi \in D_A(E^+)$, we have $r'(\varphi^k) = r(\varphi)^k$, so $\varphi^k$ fixes $K$ exactly when $f \mid k$. Part (a), applied to $E \subseteq K$ with $d = f$, gives $N(w') = N(w)^f$ for each place $w'$ of $K$ under $A$.

Let $u$ be a place of $E$ that is not split over $E^+$, and let $A$ lie over $u$. Since $\ker r'$ is ramified only at split places, either $I_A(E^+) \subseteq \ker r'$ or $D_A(E^+)$ fixes $E$. The second case would make $u$ split by part (b) of the last lemma, so the first case holds. Then $I_A(E) \subseteq I_A(E^+)$ fixes $K$. $\square$

**Corollary 3.21.9 (The field for the toral step).** The statement of [Theorem 3.21.3](/entry/unr-split-holds/) holds: for $E$, $\Omega$, $w$ split over $E^+$, $f \geq 1$ and $S$ finite, there is an abelian CM extension $K$ of $E$ in $\Omega$ with properties 1 to 3.

Lean: `UpperTheory.Gal.UnramifiedFromSplittingCriterion.unrField_holds` (also `UpperTheory.Gal.NearKilling.UnrField`).

*Proof.* This is [Theorem 3.21.3](/entry/unr-split-holds/), with the same statement. $\square$

In the toral step, $w$ is a place with $E_w \cong \mathbb{Q}_g$, so $N(w) = g$, and $f = n!$. The places of $K$ above $w$ then have norm $g^{n!}$, and cyclic base change is applied along the $S$-tower.

**Remark 3.21.10 (Formalization).** The corollary is a renaming: the statement in [UnlinkedOfType.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CharpolyFromTrace/UnlinkedOfType.lean#L112) repeats the one in [AsmUnr.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/InertiaQuadraticRamification/AsmUnr.lean#L12) word for word, and its proof cites the theorem. The theorem is `unrSplit_of` applied to seven inputs, all proved in the development: `groupStep`, `unrCharPP`, `freshSplit freshChar_holds`, `exFld`, `layerOf_holds`, `degOf` and `splitIff`. We opened the statements of these inputs and the proofs of `unrSplit_of` and `unrCharAt_of`, but not the proofs of the inputs themselves. In a layer the fresh place is a place of $E$, while the layer lemma works with a place of $E^+$; the passage between them is inside `layerOf_holds`, which we did not open.

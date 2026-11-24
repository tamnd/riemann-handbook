---
title: Lemma K and integral Satake parameters
decls:
  - UpperTheory.V.ZK.sClassOf
  - UpperTheory.V.ZK.lemmaK
  - UpperTheory.V.ZK.bOdd
  - UpperTheory.V.ZK.lemmaK_of_litN_alt
  - UpperTheory.V.ZK.lemmaK_litN_alt
  - UpperTheory.V.Z.Int.slopeAllOf
  - UpperTheory.V.Z.Int.slopeAll
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lemma K and integral Satake parameters

This section proves two inputs of [the window bound from the extended hypotheses](/entry/vwin-of-hypotheses-h-e-alt/). The first is Lemma K of section 1, the bound on the size of $H^2$ of a totally complex field with coefficients in a Tate twist. The proof goes through $H^1$, and it bounds the number of Kummer classes with homology classes of $\mathrm{GL}_N$ over a ring of integers. The second input is an integrality statement for the Satake parameters of a polarized cuspidal representation of $\mathrm{GL}_n$ over a CM field.

### Lemma K

Let $L$ be a totally complex number field with $r_2$ complex places. For a ring $R$ and $d, n \ge 1$, let $\psi_d \colon \mathrm{GL}_n(R) \to \mathrm{GL}_{dn}(R)$ be the block diagonal map $A \mapsto 1_d \otimes A$, and let $\iota \colon \mathrm{GL}_n(R) \to \mathrm{GL}_{dn}(R)$ be the map $A \mapsto \operatorname{diag}(A, 1)$. Fix $l \ge 1$. For a class $x \in H_m(\mathrm{GL}_n(R), \mathbb{Z})$ put $z_0(x) = x$ and

$$z_{t+1}(x) = (\psi_l)_* z_t(x) - l^{t+2}\, \iota_* z_t(x).$$

So $z_t(x)$ lies in the homology of $\mathrm{GL}_{l^t n}(R)$.

**Theorem 8.15.1 (Rank bound in odd degree).** Let $k$ be even with $k + 1 < r_2$, let $l \ge 1$ and $n \ge 2(k+1) + 4$. Then the classes $z_k(x)$, for $x \in H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L), \mathbb{Z})$, span a $\mathbb{Z}$-module of rank at most $r_2$.

Lean: `UpperTheory.V.ZK.bOdd`.

*Proof.* This is the rank bound for the same sequence in the theory of stable homology, moved to the present definitions of $\psi_d$ and $z_t$. $\square$

The bound has the shape of the rank formula of Borel for the odd $K$-groups of $\mathcal{O}_L$: for a totally complex field and even $k \ge 2$, the group $K_{k+1}(\mathcal{O}_L)$ has rank $r_2$ (A. Borel, *Stable real cohomology of arithmetic groups*, Ann. Sci. Ec. Norm. Sup. 7 (1974)).

Let $F/L$ be a layer of the cyclotomic $l$-tower: $F$ contains a root of unity $\zeta$ of order $l^\nu$, and $\gamma$ is a generator of $\operatorname{Gal}(F/L)$ that acts on $\zeta$ through $1 + l^c$. For $\alpha \in F^\times$ and an integer $a$, let $N_a(\alpha)$ be the twisted norm of $\alpha$ for $\gamma$ with weight $a$. A finite field $k$ with a ring map $r \colon \mathcal{O}_F \to k$ that is onto on $\mathcal{O}_L$ is a residue field of $F$ over $L$. We use additive invariants $\theta$ of chains of $\mathrm{GL}(V)$ over finite fields with values in $\mathbb{Z}/l^\nu$, normalized by their value on an explicit cycle $z_c$ of $\mathbb{Z}/q$.

**Lemma 8.15.2 (Classes from Kummer elements).** Assume the bar chain facts ($\partial^2 = 0$, functoriality, prism homotopies for conjugation and their multiplicativity, and that $z_c$ is a cycle), the relation fact, the eta fact and the Steinberg fact. Let $2e + 3 < l^c$, and let $\alpha \in F^\times$ satisfy the divisor condition for $\gamma$ and $(1 + l^c)^{e+1}$. Then there are $N$, a cycle $y$ of degree $2e + 3$ in the chains of $\mathrm{GL}_N(\mathcal{O}_L)$ with coefficients $\mathbb{Z}/l^\nu$, and $b \in \mathcal{O}_F$ with $b \ne 0$, with this property. For each residue field $r \colon \mathcal{O}_F \to k$ with $r(b) \ne 0$ and each normalized additive $\theta$, there is a residue $u \in k^\times$ of $N_{(1+l^c)^{e+1}}(\alpha)$ such that $\theta(r(y))$ is a fixed constant times $v(u)$, where $v$ is the character of $k^\times$ fixed by the normalization.

Lean: `UpperTheory.V.ZK.sClassOf`.

*Proof.* The cycle $y$ is built from classes of lattice blocks. The proof joins seventeen facts on these classes: the chain property, freeness, triviality, the action of $\gamma$, splitting, support, local lattices, the roots of unity, integrality, valuations, two comparisons of orders, divisibility and valuation of the elements $\beta$ that enter the blocks, representatives, and units. Together they give the cycle and the element $b$. $\square$

**Theorem 8.15.3 (Lemma K from duality).** Assume the rank bound in odd degree, Poitou-Tate duality, local finiteness and local Tate duality. Then Lemma K holds with some constant $C_K$.

Lean: `UpperTheory.V.ZK.lemmaK`.

*Proof.* The proof has five parts.

1. *Chains.* From the bar chain facts and a cocycle on $k^\times$ for each finite field $k$ we get, for each finite field, an additive invariant $\theta$ with the normalized value on $z_c$.
2. *Classes.* The lemma gives, for each Kummer element $\alpha$ of a layer, a cycle $y$ whose values under $\theta$ detect the residues of a twisted norm of $\alpha$.
3. *Upper bound.* By the rank bound in odd degree, the number of such values is at most $(l^\nu)^{r_2}$ times two orders of torsion subgroups of $H_m(\mathrm{GL}_N(\mathcal{O}_L), \mathbb{Z})$.
4. *Counting.* An element that is an $l^\nu$-th power at enough residue fields is an $l^\nu$-th power. So the values of step 3 bound the number of $\alpha$ that are distinct modulo $l^\nu$-th powers. With a count of classes, a bound for the Tate-Shafarevich part, a bound over the layers and a torsion bound, this gives a constant $C$ such that $s \log l \le \exp((2En)^C \log(2D))$. Here $s$ is the length of the classes in $H^1(G_L, \mathbb{Q}_l/\mathbb{Z}_l(-E))$ that are trivial on the decomposition groups above $l$ and unramified elsewhere.
5. *From $H^1$ to $H^2$.* Poitou-Tate duality and local Tate duality relate $H^2(G_S, \mathbb{Z}_l(\chi^{e+1}))$ to the group of step 4 and to local terms. Local finiteness bounds the local terms. This gives Lemma K.

The three duality statements enter only in step 5. $\square$

**Corollary 8.15.4 (Lemma K from the rank n package).** Assume the rank bound in odd degree and the rank $n$ package. Then Lemma K holds with some constant $C_K$. Under the rank $n$ package alone, Lemma K holds with some constant $C_K$.

Lean: `UpperTheory.V.ZK.lemmaK_of_litN_alt` (also `UpperTheory.V.ZK.lemmaK_litN_alt`, the form without the rank bound as a hypothesis).

*Proof.* The rank $n$ package contains Poitou-Tate duality, local finiteness and local Tate duality, and the theorem applies. For the second form, the rank bound holds by its theorem. $\square$

### Integral Satake parameters

Let $E$ be a CM field, $n \ge 1$ and $m_1 > m_2 > \dots > m_n$ integers. Let $\pi$ be a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb{A}_E)$ whose infinitesimal character at each complex place is the multiset of the numbers $\frac{n-1}{2} + m_i$, and that is polarized: $(\pi, \chi)$ is a polarized pair for some character $\chi$. Let $w$ be a finite place of $E$ of norm $q$ at which $\pi$ has Satake parameters $\alpha_1, \dots, \alpha_n$, and put $b_i = q^{(n-1)/2} \alpha_i$.

**Definition 8.15.5 (Integral slopes).** The slope statement says that for all such $\pi$, $w$ and $i$, the number $q^a b_i$ is an algebraic integer for each integer $a \ge \max_j m_j$, and $q^a b_i^{-1}$ is an algebraic integer for each integer $a \ge -\min_j m_j$. The slope statement at split places, for a class $s$ of representations, gives the same bounds in the form $|\iota^{-1}(q^a b_i)| \le 1$ for each prime $\ell$ and each isomorphism $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$, but only at places $w$ that split over the maximal totally real subfield, and only for $\pi$ in $s$.

The quadratic lifting statement says: for a quadratic extension $M/K$ of totally complex fields and a cuspidal $\pi$ on $\mathrm{GL}_a(\mathbb{A}_K)$, if some place of $M$ that ramifies over $K$ lies over a place where $\pi$ has Satake parameters, then $\pi$ has a cuspidal lift to $\mathrm{GL}_a(\mathbb{A}_M)$ that matches Satake parameters, infinitesimal characters and local components. It has the shape of quadratic base change (J. Arthur and L. Clozel, *Simple algebras, base change, and the advanced theory of the trace formula*, Ann. of Math. Stud. 120, 1989), but we have not compared the hypotheses.

**Theorem 8.15.6 (Slopes at all places from split places).** Assume quadratic lifting and the slope statement at split places for the good class. Then the slope statement holds.

Lean: `UpperTheory.V.Z.Int.slopeAllOf`.

*Proof.* The $m_i$ are distinct, so $\pi$ is regular algebraic. There is a CM field $K \supset E$ with $[K : E] = 2$ such that the places of $K$ above $w$ split over the maximal totally real subfield, some place of $K/E$ ramifies over a place where $\pi$ is unramified, and every lift of $\pi$ to $K$ is good at $2$. Quadratic lifting gives a cuspidal lift $P$ of $\pi$ to $K$, and the base change of a polarized pair is polarized with the same weights. There is a place $w'$ of $K$ above $w$ with $E_w \cong K_{w'}$. Then $w'$ has norm $q$, and $P$ has the Satake parameters $\alpha_i$ at $w'$. The slope statement at split places, for $P$ at $w'$ and $\ell' = 2$, gives $|\iota^{-1}(q^a b_i)| \le 1$ for all $\ell$ and $\iota$. A number whose image under every such $\iota^{-1}$ has absolute value at most $1$ is an algebraic integer. The same argument works for $b_i^{-1}$. $\square$

The descent statement off a set $T$ says: a conjugate self-dual $\pi$ whose character $\chi$ is a power of the quadratic character matches an automorphic representation of a unitary group in $a$ variables, outside a finite set $T$ of non-split places that avoids any given finite set.

**Corollary 8.15.7 (Integral slopes).** Assume quadratic lifting and descent off $T$. Then the slope statement holds.

Lean: `UpperTheory.V.Z.Int.slopeAll`.

*Proof.* Descent off $T$ gives the slope statement at split places for the conjugate self-dual class. A twist by a suitable character, unramified at the split place, moves a good $\pi$ into this class and moves its Satake parameters by the values of the character. So the slope statement at split places holds for the good class, and the theorem applies. $\square$

**Remark 8.15.8 (Formalization).** The rank bound `bOdd` in [BOdd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/BOdd.lean#L3), a file of three lines, is a new name for `PositivityTheory.KB.bOdd_zk`. Its hypothesis on $l$ is only $l > 0$, so $l$ need not be prime. The proof of `lemmaK` in [LemmaKOfLitN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/LemmaKOfLitN.lean#L28) feeds 21 steps to `lemmaK_of_steps`. Five of these steps are proved by theorems that are all named `intersectionNumber_baseChange`, for example in [FinSRel.lean](lean:Development/EtaleCohomology/CyclotomicDiscriminants/FinSRel.lean#L6), and no intersection number appears in their statements. The step on the Tate-Shafarevich part is proved by `PositivityTheory.QuaternionShaBounds.sSha`, and no quaternion algebra appears in it. The file [DenseThresholdCases/LemmaKOfLitN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LemmaKOfLitN.lean#L12) has the same base name as the file of `lemmaK`, and `lemmaK_litN_alt` in [KFinal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KFinal.lean#L11) only calls `lemmaK_of_litN_alt` with `bOdd`. The lemma `sClassOf` in [SClassOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/SClassOf.lean#L21) is one application of `cJoin` to seventeen lemmas. In [SlopeAll.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/IntegralDeterminants/SlopeAll.lean#L11) the proof is `slopeAllOf hL (slopeGood (slopeCsd hD))`, and in [SlopeAllOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/IntegralDeterminants/SlopeAllOf.lean#L152) the split slope statement is used only at $\ell' = 2$. We have not unfolded the predicates `Lay`, `DivDel`, `CuspSub` and `PolarizedPair`.

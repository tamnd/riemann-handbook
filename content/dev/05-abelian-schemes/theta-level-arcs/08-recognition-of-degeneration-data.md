---
title: Recognition of degeneration data
decls:
  - GlobalTheory.T.degenerationRecognition_of_abelianPartsIsoLabels
  - GlobalTheory.Ex.Recognition.urec_of_abelian
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Recognition of degeneration data

The recognition theorem says that two sets of degeneration data over a complete field are isomorphic as soon as their points of level $n^j$ and their theta null values match, for one odd prime $n$. In this section we reduce the recognition theorem to the case in which an isomorphism of the abelian parts is already given. The reduction combines four results on matchings: the matched parts have the same dimension, the lattices are isomorphic in a way that respects the terms of the theta series, an isomorphism of abelian parts extends to an isomorphism of the full numerical data, and such an extension respects the labels of the points. The theorem enters the proof at [EveryCharacter from the literature](/step/every-character-of-literature/). For the background on degeneration data see [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) in Volume 1.

### Numerical data and matchings

Let $R$ be a domain. A *degeneration presentation* $D$ over $R$ consists of a polarized abelian scheme $A$ over $R$ with line bundle $L$, a rigidification of $L$ at the origin, a cubical structure and a symmetry of $L$, a free abelian group $\mathsf{X}$ of finite rank, a homomorphism $c : \mathsf{X} \to A(R)$ and generators $\psi(\chi)$ of $L$ at the points $c(\chi)$. We write $g$ for the relative dimension of $A$. The conditions that $\psi$ is even and that the associated form $\tau$ is bimultiplicative are hypotheses below.

**Definition 6.8.1 (Numerical datum).** Let $O$ be a ring. A *numerical datum* $N$ over $O$ consists of:

1. a commutative group $A_N$ with a cubical function $\theta : A_N^3 \to O^\times$, a function $\sigma : A_N \to O^\times$ with the symmetry laws, and a theta function $\vartheta : A_N \to O$;
2. a free abelian group $\mathsf{X}_N$ of finite rank, a homomorphism $c : \mathsf{X}_N \to A_N$ and a function $\psi : \mathsf{X}_N \to O^\times$ that is even and whose quotient $\tau(a, b) = \psi(a + b)/\psi(a)\psi(b)$ is bimultiplicative up to $\theta$.

Lean: `GlobalTheory.Ex.NumD`.

A *numerical image* $\nu$ of $D$ in $N$ over a field $F$ that is an algebra over $\operatorname{Frac} R$ is a choice of charts of $L$, an isomorphism $A_N \cong A(F)$ and an isomorphism $\mathsf{X}_N \cong \mathsf{X}$ that carry $c$, $\theta$, $\sigma$ and $\vartheta$ of $N$ to the values of $c$, of the cubical structure, of the symmetry and of a generating section of $L$, read in the charts.

The group $\mathrm{Gt}(N)$ of *theta translations* consists of the pairs $(b, s)$ with $b \in A_N$ and $s : \mathsf{X}_N \to O^\times$ such that $s(\chi + \chi')\,\theta(c\chi, c\chi', b) = s(\chi)\, s(\chi')$. Each $y \in \mathsf{X}_N$ gives the translation $\iota(y) = (c(y), \tau(y, \cdot))$. The *points of level $k$* of $N$ are the pairs $(x, g)$ with $x \in \mathsf{X}_N$ and $g \in \mathrm{Gt}(N)$ such that $g^k = \iota(x)$. Two of them are *equivalent* if they differ by $(kz, \iota(z))$ for some $z$. Each point $p$ of level $m^2$ has a theta null value $\vartheta_m(p) = \sum_\chi \vartheta_m(p, \chi)$, a sum of terms built from $\psi$, $s$ and $\vartheta$.

**Definition 6.8.2 (Integral and torsion conditions).** Let $C$ be a normed field and $q$ a real quadratic form on $\mathsf{X}_N$. The datum $N$ is *integral for $q$* if $|\theta| = |\sigma| = 1$, $|\vartheta| \leq 1$, $|\psi(\chi)| = e^{-q(\chi)}$, and $q(\chi) \to \infty$ as $\chi$ leaves finite sets. It satisfies the *torsion conditions* for an odd prime $n$ and an integer $g$ if $A_N$ is $n$-divisible, its $n^j$-torsion is $(\mathbb{Z}/n^j)^{2g}$ with a nondegenerate Weil pairing, each coset of the $n$-torsion carries a value of $\vartheta$ of norm $1$, and the values of level $n^j$ separate points.

Lean: `GlobalTheory.Ex.NumD.Int` (also `GlobalTheory.Ex.NumB.Tors`, the torsion conditions).

**Definition 6.8.3 (Matching).** Let $N$ and $N'$ be numerical data over $C$ and let $n$ be a prime. A *matching* $\mu$ of $N$ and $N'$ at $n$ is a family of relations $r_k$ between the points of level $k$ of $N$ and of $N'$ such that, at the levels $k = n^j$, each point of either side is related to a point of the other side; $r_k$ is multiplicative, compatible with equivalence in both directions, injective up to equivalence, compatible with the inclusions of levels $k \mid kk'$, and preserves the Weil pairings; and there is $c_0 \neq 0$ in $C$ with $\vartheta'_{n^j}(p') = c_0\, \vartheta_{n^j}(p)$ whenever $p$ and $p'$ are related at level $n^{2j}$.

Lean: `GlobalTheory.Ex.Match`.

We use these conditions on $\mu$.

1. The condition $\mathsf{A}$: $|c_0| = 1$, and related points lie both or neither in $k\mathsf{X}$, and are both or neither equivalent to a torus point $(0, (1, s))$.
2. For an isomorphism $e : \mathsf{X}_N \to \mathsf{X}_{N'}$, the condition $\mathsf{B}(e)$: if $(x, g)$ and $(x', g')$ are related at level $n^j$, then $x' \equiv e(x)$ modulo $n^j$.
3. The condition $\mathsf{Term}(e)$: for related torus points at level $n^{2j}$, the terms satisfy $\vartheta'_{n^j}(p', e\chi) = c_0\, \vartheta_{n^j}(p, \chi)$ for all $\chi$.
4. For an isomorphism $I$ of the abelian parts, the condition $\mathsf{OnB}(I)$: related torus points have $b' = I(b)$. For an isomorphism $J$ of numerical data, $\mathsf{OnG}(J)$ says that related torus points have translations related by $J$, and $\mathsf{OnQ}(J)$ says that every pair $(p, p')$ with $x' = J(x)$ and $g'$ related to $g$ by $J$ is in $r_{n^j}$.

An isomorphism of the abelian parts $I : (A_N, \theta, \sigma, \vartheta) \to (A_{N'}, \theta', \sigma', \vartheta')$ is a group isomorphism $\varphi$ with a gauge $h : A_N \to O^\times$ and a constant $\lambda$ that carry $\theta$, $\sigma$ and $\vartheta$ to $\theta'$, $\sigma'$ and $\lambda h \vartheta$. An isomorphism of numerical data adds an isomorphism $e$ of lattices compatible with $c$ and $\psi$.

**Definition 6.8.4 (Geometric isomorphism).** Let $\nu$ and $\nu'$ be numerical images of $D$ and $D'$ in $N$ and $N'$ over $F$, and let $I$ be an isomorphism of the abelian parts. We say $I$ is *geometric* if there are an isomorphism $\varphi : A_F \to A'_F$ over $F$, an isomorphism $w$ of $L$ with $\varphi^* L'$ that is a generator, and values $w_v(x) \in F$ such that $\varphi$ carries the point of $x$ to the point of $I(x)$, $w_v(x)$ is the value of $w$ at the point of $x$ in the charts, and $I.h(x)\, w_v(1) = w_v(x)$ for all $x$.

Lean: `GlobalTheory.Ex.GeoIso`.

### The two statements

Both statements quantify over the same data: a domain $R$; presentations $D$ and $D'$ over $R$ with $\psi$ even and $\tau$ bimultiplicative; an algebraically closed, complete, ultrametric, nontrivially normed field $C$ over $\operatorname{Frac} R$; numerical data $N$ and $N'$ over $C$ with numerical images $\nu$ and $\nu'$; quadratic forms $q$ and $q'$ for which $N$ and $N'$ are integral; an odd prime $n$ with $|n| = 1$ such that $N$ satisfies the torsion conditions for $n$ and $g(D)$ and $N'$ for $n$ and $g(D')$; and a matching $\mu$ of $N$ and $N'$ at $n$.

**Definition 6.8.5 (Recognition statement).** The *recognition statement* says: for all such data, there is an isomorphism $J$ of numerical data with $\mathsf{OnQ}(J)$ whose abelian part is geometric for $\nu$ and $\nu'$.

Lean: `GlobalTheory.Ex.URecSt`.

**Definition 6.8.6 (Recognition of abelian parts).** The *recognition statement for abelian parts* says: for all such data, if $\mathsf{A}$ holds, $g(D) = g(D')$, and $e$ is an isomorphism of lattices with $\mathsf{B}(e)$ and $\mathsf{Term}(e)$, then there is an isomorphism $I$ of the abelian parts with $\mathsf{OnB}(I)$, constant $\lambda = c_0$, and $I$ geometric for $\nu$ and $\nu'$.

Lean: `GlobalTheory.Ex.UrCSt`.

### Inputs

The four inputs below are proved elsewhere in the Lean development. In each, $C$ is an algebraically closed, complete, ultrametric, nontrivially normed field, $N$ and $N'$ are integral for $q$ and $q'$ and satisfy the torsion conditions for an odd prime $n$ with $|n| = 1$ and integers $g$ and $g'$, and $\mu$ is a matching at $n$.

**Theorem 6.8.7 (Matched parts).** The matching satisfies $\mathsf{A}$, and $g = g'$.

Lean: `GlobalTheory.T.thetaRecognition_matched_parts_dim_eq`.

**Theorem 6.8.8 (Lattice and terms).** If $\mathsf{A}$ holds, there is an isomorphism $e$ of lattices with $\mathsf{B}(e)$ and $\mathsf{Term}(e)$.

Lean: `GlobalTheory.T.thetaRecognition_lattice_iso_and_terms_agree`.

**Theorem 6.8.9 (Extension to the periods).** If $\mathsf{A}$, $\mathsf{B}(e)$ and $\mathsf{Term}(e)$ hold and $I$ is an isomorphism of abelian parts with $\mathsf{OnB}(I)$, then there is an isomorphism $J$ of numerical data with abelian part $I$, lattice part $e$, and $\mathsf{OnG}(J)$.

Lean: `GlobalTheory.T.exists_numD_iso_onG_of_allMatch`.

**Theorem 6.8.10 (Labels).** If $\mathsf{A}$ holds and $J$ is an isomorphism of numerical data with $\mathsf{B}(J.e)$, $\mathsf{OnG}(J)$ and constant $\lambda = c_0$, then $\mathsf{OnQ}(J)$ holds.

Lean: `GlobalTheory.T.thetaRecognition_labels_agree_of_iso`.

### The reduction

**Theorem 6.8.11 (Recognition from abelian parts).** The recognition statement for abelian parts implies the recognition statement.

Lean: `GlobalTheory.T.degenerationRecognition_of_abelianPartsIsoLabels` (also `GlobalTheory.Ex.Recognition.urec_of_abelian`, a second name).

*Proof.* Fix the data of the recognition statement. By the theorem on matched parts, $\mu$ satisfies $\mathsf{A}$ and the dimensions agree, $g(D) = g(D')$. By the theorem on lattice and terms, there is an isomorphism $e$ of lattices with $\mathsf{B}(e)$ and $\mathsf{Term}(e)$. The recognition statement for abelian parts, applied to $\mathsf{A}$, the equality of dimensions and $e$, gives an isomorphism $I$ of abelian parts with $\mathsf{OnB}(I)$, constant $c_0$, and $I$ geometric. By the extension to the periods, there is an isomorphism $J$ of numerical data with abelian part $I$, lattice part $e$ and $\mathsf{OnG}(J)$. Then $\mathsf{B}(J.e) = \mathsf{B}(e)$ holds and the constant of $J$ is $c_0$, so the theorem on labels gives $\mathsf{OnQ}(J)$. The abelian part of $J$ is $I$, which is geometric. $\square$

**Remark 6.8.12 (Formalization).** The proof is in [DegenerationRecognitionOfAbelianPartsIsoLabels.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/DegenerationRecognitionOfAbelianPartsIsoLabels.lean#L17), and the statement form is a `first | exact ...` block in [DegenerationRecognitionOfAbelianPartsIsoLabelsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/DegenerationRecognitionOfAbelianPartsIsoLabelsStatement.lean#L11). The two statements are defined in [AdmissibleBaseOfCompleteDvr.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/AdmissibleBaseOfCompleteDvr.lean#L87). The four inputs are stated with `AllMatch`, which does not mention $R$, $D$, $D'$, $\nu$ or $\nu'$; the presentations and the numerical images enter only through the statement for abelian parts and through the condition `GeoIso`. The evenness of $\psi$ and the bimultiplicativity of $\tau$ are passed to that statement and are not used otherwise. The equation $J.e = e$ and the equation of the abelian part are used by `subst` at line 23. We did not unfold `PsiEven`, `TauBimult`, `NumOf`, `IsGen` or the cubical structure.

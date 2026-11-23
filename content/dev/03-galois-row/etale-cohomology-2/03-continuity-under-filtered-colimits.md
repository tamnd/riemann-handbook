---
title: Continuity under filtered colimits
decls:
  - LateralTheory.Fin.Cont.intersectionNumber_baseChange
  - LateralTheory.Fin.Cont.etale_kunneth_cohomology_continuous_under_limits_in_continuity_assembl
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Continuity under filtered colimits

Let $X$ be a quasi-compact and separated scheme over a ring $R$, and let $D = \varinjlim D_j$ be a filtered colimit of $R$-algebras. Then the étale cohomology of $X \times_R \operatorname{Spec} D$ is the colimit of the cohomology of the schemes $X \times_R \operatorname{Spec} D_j$. This section proves this for the cohomology of the code with coefficients $\mathbb{Z}/q(i)$, from the same statement for affine schemes, which the code takes as an axiom. The proof is an induction on the number of affine opens that cover $X$, with the Mayer-Vietoris sequence and the five lemma. The result is used in [the theorem that classes are killed on an étale neighbourhood](/entry/cont-of/).

The cohomology $H^n(X, F)$ and the sheaves $\mathbb{Z}/q(i)$ are as in the section before [the theorem on the Kummer class](/entry/etale-kummer-class-explicit-cocycle-holds-of/). Each sheaf $F$ has a chosen injective resolution $F \to I^\bullet$. A map of schemes $f : Y \to X$ gives a pullback $f^* : H^n(X, F) \to H^n(Y, F)$. A [[filtered category|975PMY4FG8]] and a [[colimit|BJS1CGTKQ5]] are as in category theory.

**Theorem (Continuity, standard form).** Let $X_0$ be a quasi-compact and quasi-separated scheme, let $(X_j)$ be a filtered inverse system of $X_0$-schemes with affine transition maps, and let $X = \varprojlim X_j$. Let $F$ be a sheaf on $X_0$. Then $H^n(X, F) = \varinjlim_j H^n(X_j, F)$ for all $n$.

This is in J. S. Milne, *Étale Cohomology*, Chapter III, §1. The code proves the case $X_j = X_0 \times_R \operatorname{Spec} D_j$ with $X_0$ separated over $\operatorname{Spec} R$ and $F = \mathbb{Z}/q(i)$, from the affine case.

**Definition (Continuity of a functor).** Let $(D_j)$ be a filtered diagram with a cocone $D_j \to D$, and let $G$ be a functor to abelian groups. We say that $G$ is *continuous* on the cocone if two conditions hold. First, each $x \in G(D)$ is the image of some $y \in G(D_j)$. Second, if $y \in G(D_j)$ maps to $0$ in $G(D)$, then $y$ maps to $0$ in $G(D_k)$ for some $j \to k$.

If the cocone is a colimit, continuity says that $\varinjlim G(D_j) \to G(D)$ is bijective.

**Definition (The two axioms).** The code uses two axioms on its cohomology.

1. *Affine continuity.* For each filtered diagram of rings $(D_j)$ with colimit $D$ and all $n$, $i$, the functor $A \mapsto H^n(\operatorname{Spec} A, \mathbb{Z}/q(i))$ is continuous on the cocone $D_j \to D$, for the classes on rings in which $q$ is a unit.
2. *Smooth descent.* For each smooth surjective map $f : Y \to X$ and each sheaf $F$, the Čech nerve of $f$ computes $H^\bullet(X, F)$.

The first axiom is the affine case of the standard theorem above. We did not unfold the precise form of the second axiom in the code.

**Theorem (Continuity).** Assume the two axioms. Let $q \ne 0$, let $R$ be a ring in which $q$ is a unit, and let $p : X \to \operatorname{Spec} R$ be quasi-compact and separated. Let $(D_j)$ be a filtered diagram of $R$-algebras with colimit $D$. For an $R$-algebra $A$ write $X_A = X \times_{\operatorname{Spec} R} \operatorname{Spec} A$. Then for all $n, i \in \mathbb{Z}$ the functor $A \mapsto H^n(X_A, \mathbb{Z}/q(i))$ is continuous on the cocone $D_j \to D$.

Lean: `LateralTheory.Fin.Cont.etale_kunneth_cohomology_continuous_under_limits_in_continuity_assembl` (also `LateralTheory.Fin.Cont.intersectionNumber_baseChange`, a second name).

We first describe the cohomology of a scheme by sections, and then build the Mayer-Vietoris sequence.

**Lemma (Dictionary).** Let $X$ be a scheme and $I$ a complex of sheaves. Each class in $H^n(X, I)$ is the class of a cocycle whose only nonzero component is $\alpha_0(x) = x^*z$, for a section $z \in I^n(X)$ with $dz = 0$. The class of $z$ is zero if and only if $z = dy$ with $y \in I^{n-1}(X)$. Sums and negatives of classes correspond to sums and negatives of sections.

Lean: `LateralTheory.KummerTheory.Dict_of'`.

*Proof.* A scheme gives a simplicial presheaf that is constant in the simplicial direction. The code first shows that each cocycle is cohomologous to a normalized one, with all components of positive simplicial degree zero. A normalized cocycle is determined by $z = \alpha_0(\mathrm{id}_X)$, and the cocycle condition becomes $dz = 0$. A coboundary of a normalized cochain gives $z = dy$. So $H^n(X, I)$ is the cohomology of the complex $I^\bullet(X)$ of global sections. $\square$

**Definition (Mayer-Vietoris square).** A *Mayer-Vietoris square* is a pullback square of schemes
$$\begin{array}{ccc} W & \xrightarrow{a} & U \\ {\scriptstyle b}\downarrow & & \downarrow{\scriptstyle f} \\ V & \xrightarrow{g} & X \end{array}$$
in which $f$ and $g$ are [[open immersions|GFC5YKSN5H]] and each point of $X$ lies in the image of $f$ or of $g$.

So $X = U \cup V$ and $W = U \cap V$.

**Lemma (Mayer-Vietoris sequence).** Let a Mayer-Vietoris square be given, and let $F$ be a sheaf. Then there are maps $\delta : H^n(W, F) \to H^{n+1}(X, F)$ that make the sequence
$$\begin{aligned} \cdots \to H^n(X, F) &\xrightarrow{(f^*, g^*)} H^n(U, F) \oplus H^n(V, F) \\ &\xrightarrow{a^* - b^*} H^n(W, F) \xrightarrow{\delta} H^{n+1}(X, F) \to \cdots \end{aligned}$$
exact. For a family of Mayer-Vietoris squares indexed by a category $K$, the sequences are natural in $K$.

Lean: `LateralTheory.KummerTheory.MVnatPf.MVnat_of` (also `LateralTheory.KummerTheory.ExactPf.Exact_of` and `LateralTheory.KummerTheory.ContCut.Delta_of`).

*Proof.* By the dictionary, it is enough to work with the complex of sections of the injective resolution $I$ of $F$. Two facts on sections give the result. First, the [[sheaf|RT8A8FJ566]] property for the covering $\{U, V\}$ of $X$: sections of $I^n$ on $U$ and $V$ that agree on $W$ glue to a unique section on $X$. Second, each injective sheaf $G$ restricts surjectively along a monomorphism $W \to U$, such as an open immersion. We give the argument for this fact; we did not open its proof in the code. The reason is that the map of free sheaves $R[W] \to R[U]$ is then a monomorphism, and $G(U) = \operatorname{Hom}(R[U], G)$ maps onto $\operatorname{Hom}(R[W], G) = G(W)$ because $G$ is injective. So the sequence of complexes
$$0 \to I^\bullet(X) \to I^\bullet(U) \oplus I^\bullet(V) \to I^\bullet(W) \to 0$$
is exact, and its long exact sequence is the Mayer-Vietoris sequence. The map $\delta$ is the connecting map. Write $w = s|_W$ with $s \in I^n(U)$. Then $ds$ vanishes on $W$ and glues with $0$ on $V$ to a cocycle $z$ on $X$, and $\delta[w] = [z]$. All constructions commute with pullback along maps of squares. $\square$

**Lemma (Five lemma for colimits).** Let $K$ be a category and let
$$\cdots \to X_n \to U_n \oplus V_n \to W_n \to X_{n+1} \to \cdots$$
be a long exact sequence of functors from $K$ to abelian groups. Let $(D_j) \to D$ be a filtered cocone in $K$. If $U_n$, $V_n$ and $W_n$ are continuous on the cocone for all $n$, then so is $X_n$ for all $n$.

Lean: `LateralTheory.KummerTheory.FivePf.Five_of`.

*Proof.* If the cocone is a colimit, filtered colimits of abelian groups are exact, and the claim is the five lemma for the map from the colimit sequence to the sequence at $D$. The code proves the claim for any cocone by the same diagram chase, done on elements: the chase uses only that each element comes from some stage and that each relation holds at some later stage. We did not open the details of this chase. $\square$

**Lemma (Induction on covers).** Let $R$ be a ring and let $P$ be a property of schemes over $\operatorname{Spec} R$. Assume that $P$ holds for affine schemes. Assume that for each Mayer-Vietoris square over $\operatorname{Spec} R$, if $P$ holds for $U$, $V$ and $W$, then it holds for $X$. Then $P$ holds for each quasi-compact and [[separated|X30G4V7VAJ]] scheme over $\operatorname{Spec} R$.

Lean: `LateralTheory.KummerTheory.IndPf.Ind_of`.

*Proof.* A [[quasi-compact|41009J4M5D]] $X$ is a union of affine opens $U_1, \dots, U_m$. We use induction on $m$. For $m = 1$, $X$ is affine. For $m > 1$, put $U = U_1$ and $V = U_2 \cup \dots \cup U_m$. Then $W = U \cap V$ is the union of the opens $U_1 \cap U_k$ for $k \ge 2$. These are affine, because $X$ is separated and the intersection of two affine opens of a separated scheme is affine. So $V$ and $W$ are unions of $m - 1$ affine opens, and they are separated, as opens of $X$. By induction $P$ holds for $U$, $V$ and $W$, so for $X$. $\square$

**Lemma (Base change).** The base change of a Mayer-Vietoris square over $\operatorname{Spec} R$ along $\operatorname{Spec} A \to \operatorname{Spec} R$ is a Mayer-Vietoris square.

Lean: `LateralTheory.KummerTheory.BCPf.BC_of`.

*Proof.* Open immersions, pullback squares and joint surjectivity are stable under base change. $\square$

**Lemma (Affine case).** Assume affine continuity. Let $X$ be affine over $\operatorname{Spec} R$, with $q$ a unit in $R$. Then for all $n$, $i$ the functor $A \mapsto H^n(X_A, \mathbb{Z}/q(i))$ is continuous on each filtered colimit of $R$-algebras.

Lean: `LateralTheory.KummerTheory.AffPf.Aff_of` (also `LateralTheory.KummerTheory.AffRingPf.AffRing_of`).

*Proof.* Write $X = \operatorname{Spec} B$. Then $X_A = \operatorname{Spec}(A \otimes_R B)$, naturally in $A$, and $A \mapsto A \otimes_R B$ preserves filtered colimits. Each $A \otimes_R B$ is an $R$-algebra, so $q$ is a unit in it. Now apply affine continuity to the diagram $(D_j \otimes_R B)$. $\square$

*Proof of the theorem.* Let $P(X)$ be the property: for all $n$, the functor $A \mapsto H^n(X_A, \mathbb{Z}/q(i))$ is continuous on the cocone $D_j \to D$. By the affine case, $P$ holds for affine $X$. Let a Mayer-Vietoris square over $\operatorname{Spec} R$ be given, with $P$ for $U$, $V$ and $W$. By base change, for each $R$-algebra $A$ the square of the $(-)_A$ is a Mayer-Vietoris square, and it is natural in $A$. The Mayer-Vietoris lemma gives a long exact sequence of functors of $A$. The five lemma for colimits gives $P$ for $X$. By induction on covers, $P$ holds for each quasi-compact and separated $X$. $\square$

**Remark.** The theorem in the code assumes the axiom of smooth descent, but the proof does not use it: the first step of the proof drops it; see [ContCut.lean](lean:Development/EtaleCohomology/KummerTheory/ContCut.lean#L117). Both axioms are hypotheses of the statement, not proved results. Affine continuity is the affine case of the standard theorem, and the code does not prove it.

**Remark.** The names of the Lean statements do not fit the mathematics. One name speaks of a Künneth formula and the other of an intersection number and a base change. The theorem is a continuity statement. There is no Künneth formula and no intersection number in it.

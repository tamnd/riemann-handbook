---
title: Henselian pairs
decls:
  - UpperTheory.Et.affine_proper_base_change
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Henselian pairs

In this section we prove axiom E1: for a henselian pair $(A, I)$ in which $q$ is a unit, the map $\mathrm{sp}(A/I) \to \mathrm{sp}(A)$ is an equivalence for $\mathbb{Z}/q(i)$. This is the affine analogue of the proper base change theorem, due to O. Gabber. The proof of the proper base change theorem in sections 2 to 6 assumes it, through [Theorem 3.2.3](/entry/n78/), and [the proper base change theorem](/entry/proper-base-change/) receives it as its last input. The proof here is by descent along integral covers. It reduces the theorem to quotients of absolutely integrally closed domains, which section 11 handles without E1.

### Connectivity and Čech nerves

**Definition 3.12.1 (Connected maps).** Let $f : E \to E'$ be a map of spaces, $F$ a sheaf and $n \in \mathbb{Z}$. We say that $f$ is *$n$-connected* for $F$ if $f^* : H^j(E', F) \to H^j(E, F)$ is bijective for all $j < n$ and injective for $j = n$.

A map is an equivalence for $F$ if and only if it is $n$-connected for every $n$. In a commutative square of spaces whose two vertical maps are equivalences, the top map is $n$-connected if and only if the bottom map is $n$-connected. In particular, connectivity passes along isomorphisms of arrows.

For a map of schemes $h : Y \to X$ we write $\check{C}(h)$ for its Čech nerve. It is a space with an augmentation $\check{C}(h) \to X$, and its level $p$ is the fibre product of $p + 1$ copies of $Y$ over $X$. A map of spaces $\psi : E \to E'$ has a map $\psi_p$ at each level $p$, which we regard as a map of spaces.

We use the axioms A1, A9, B1, B2 and B4 of section 1. Other chapters of this volume prove them. Axiom B4 says that if $h : Y \to X$ is integral and surjective and $q$ is a unit on $X$, then the augmentation $\check{C}(h) \to X$ is an equivalence for $\mathbb{Z}/q(i)$.

### The inputs

We take as given the following four facts. The first two are commutative algebra, the third is a statement about spaces, and the fourth describes Čech nerves of rings.

1. *(Integral covers.)* For every ring $B$ there is an integral ring map $\varphi : B \to B'$ such that $\operatorname{Spec} \varphi$ is surjective and $B'$ is a QA ring. To construct it, let $P = \mathbb{Z}[X_b : b \in B]$, let $k$ be the kernel of the surjection $P \to B$ with $X_b \mapsto b$, and let $T$ be the integral closure of $P$ in an algebraic closure of the fraction field of $P$. Then $T$ is an absolutely integrally closed domain, $P \to T$ is integral and injective, and $B' = T/kT$ is a quotient of $T$ that is integral over $B = P/k$ with surjective spectrum.
2. *(Integral algebras over henselian pairs.)* Let $(A, I)$ be a henselian pair and $A \to B$ an integral ring map. Then $(B, IB)$ is a good pair. The proof shows that $IB$ lies in the Jacobson radical of $B$, and lifts idempotents of $B/IB$ through the lifting of factorizations of monic polynomials over $(A, I)$.
3. *(Descent step.)* Assume A1. Let $\psi : E \to E'$ be a map of spaces and $n \in \mathbb{Z}$. If every level map $\psi_p$ is $n$-connected for a sheaf $F$, and $\psi_0$ is an equivalence for $F$, then $\psi$ is $(n + 1)$-connected for $F$. The proof writes the cohomology of a space through the complex of its levels, and compares the long exact sequences of the stupid truncations of this complex for $E$ and $E'$.
4. *(Čech levels.)* Let $\varphi : B \to B'$ be integral with $\operatorname{Spec} \varphi$ surjective, and let $J \subseteq B$ be an ideal. Put $h = \operatorname{Spec} \varphi$ and $h_J = \operatorname{Spec}(B/J \to B'/JB')$. Then $h$ and $h_J$ are integral and surjective, and there is a map $\psi : \check{C}(h_J) \to \check{C}(h)$ that is compatible through the augmentations with $\mathrm{sp}(B/J) \to \mathrm{sp}(B)$. For each $p$ there is an integral ring map $\chi : B \to C$ such that $\psi_p$ is isomorphic to $\mathrm{sp}(C/JC) \to \mathrm{sp}(C)$, and $\psi_0$ is isomorphic to $\mathrm{sp}(B'/JB') \to \mathrm{sp}(B')$. Here $C$ is the tensor product of $p + 1$ copies of $B'$ over $B$.

### The theorem

**Theorem 3.12.2 (Affine proper base change).** Let $(A, I)$ be a henselian pair, and let $q \geq 1$ be a unit in $A$. Then for every $i$ the map $\mathrm{sp}(A/I) \to \mathrm{sp}(A)$ is an equivalence for $\mathbb{Z}/q(i)$. This is axiom E1.

Lean: `UpperTheory.Et.affine_proper_base_change`.

*Proof.* We fix $q$ and $i$, and we write $H^n$ for cohomology with coefficients $\mathbb{Z}/q(i)$. We say that a pair $(B, J)$ of a ring and an ideal is *admissible* if $q$ is a unit in $B$ and $(C, JC)$ is a good pair for every integral ring map $B \to C$. If $(B, J)$ is admissible and $\chi : B \to C$ is integral, then $(C, JC)$ is admissible, since $q$ maps to a unit and integral maps compose. For $m \geq 0$ let $P(m)$ be the statement: for every admissible pair $(B, J)$, the map $\mathrm{sp}(B/J) \to \mathrm{sp}(B)$ is $(m - 1)$-connected. We prove $P(m)$ for all $m$ by induction.

For $m = 0$ we must show that the map is $(-1)$-connected. By A9 all groups $H^j$ with $j < 0$ vanish on both sides, so the maps on them are bijective for $j < -1$ and injective for $j = -1$.

Suppose that $P(m)$ holds, and let $(B, J)$ be admissible. By fact 1 there is an integral map $\varphi : B \to B'$ with surjective spectrum and $B'$ a QA ring. Let $h$, $h_J$ and $\psi$ be as in fact 4.

Each level $\psi_p$ is isomorphic to $\mathrm{sp}(C/JC) \to \mathrm{sp}(C)$ for an integral map $\chi : B \to C$. The pair $(C, JC)$ is admissible, so by $P(m)$ this map is $(m - 1)$-connected, and hence so is $\psi_p$. The level $\psi_0$ is isomorphic to $\mathrm{sp}(B'/JB') \to \mathrm{sp}(B')$. Here $B'$ is a QA ring, $q$ is a unit in $B'$, and $(B', JB')$ is good because $(B, J)$ is admissible. By [Theorem 3.11.6](/entry/a33/) this map is an equivalence, and hence so is $\psi_0$. Fact 3 now says that $\psi$ is $m$-connected.

We have a commutative square
$$
\begin{array}{ccc}
\check{C}(h_J) & \xrightarrow{\ \psi\ } & \check{C}(h) \\
\downarrow & & \downarrow \\
\mathrm{sp}(B/J) & \longrightarrow & \mathrm{sp}(B)
\end{array}
$$
whose vertical maps are the augmentations. The maps $h$ and $h_J$ are integral and surjective by fact 4, and $q$ is a unit on $\operatorname{Spec} B$ and on $\operatorname{Spec}(B/J)$. By B4 both vertical maps are equivalences. Hence the bottom map is $m$-connected, which proves $P(m + 1)$.

Now let $(A, I)$ be a henselian pair with $q$ a unit in $A$. By fact 2 the pair $(A, I)$ is admissible. Let $n \in \mathbb{Z}$, and choose $m \geq 0$ with $m \geq n + 2$. By $P(m)$ the map $\mathrm{sp}(A/I) \to \mathrm{sp}(A)$ is $(m - 1)$-connected, and $n < m - 1$, so it is bijective on $H^n$. $\square$

The proof uses B1 and B2 only through the theorem of section 11, and it uses fact 2 only at the end. The induction runs over all admissible pairs at once, because the levels of the Čech nerve give new pairs $(C, JC)$ that need not be henselian.

**Remark 3.12.3 (Formalization).** The statement E1 asks only that $q$ is a unit in $A$, and so it includes $q = 0$. In that case $A$ is the zero ring, $A \to A/I$ is an isomorphism, and the proof treats this case first. The theorem is a general descent theorem applied to the five axioms and to the five facts used here, namely the four facts above and the theorem of section 11 ([EtaleCohomologyDescentOfCechCover.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomologyDescentOfCechCover.lean#L61)). Each of the five facts is the last step of a chain in its own file of the folder `EtaleAxioms`, and in each file this last step has the name `intersectionNumber_baseChange`, which has no relation to intersection numbers ([AffineProperBaseChange.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/AffineProperBaseChange.lean#L26)). A second proof of the same descent argument, with all axioms of section 1 as hypotheses, is in [EtaleDegreeZeroCohomologyEquivLocallyConstantFun.lean](lean:Development/EtaleCohomology/EtaleSheaves/EtaleDegreeZeroCohomologyEquivLocallyConstantFun.lean#L116); the chapter does not use it. We have not unfolded the proofs of facts 2 and 3; the sketches above follow the names of their steps.

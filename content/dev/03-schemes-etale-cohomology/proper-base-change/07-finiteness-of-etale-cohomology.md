---
title: Finiteness of étale cohomology
decls:
  - UpperTheory.Et.EtaleTopology.top
  - UpperTheory.Et.e4
  - UpperTheory.Et.etale_finiteness_of_duality
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finiteness of étale cohomology

In this section we prove that the étale cohomology of a proper scheme over an algebraically closed field is finite, for the coefficients $\mathbb{Z}/q(i)$. This is the axiom E4 of the first section. The Galois row uses it through the step [VFin holds](/entry/v-fin-holds/) of the chapter on Galois representations. The proof is an induction on the degree and on the dimension. Curves are the base case, and a fibration by curves reduces a scheme of dimension $d$ to schemes of smaller dimension. Proper base change and the Kummer sequence are the main tools.

**Theorem 3.7.1 (Finiteness).** Let $k$ be an algebraically closed field and let $q \geq 1$ be an integer that is a unit in $k$. Let $X$ be a proper scheme over $k$. Then for all $n, i \in \mathbb{Z}$ the group $H^n(X, \mathbb{Z}/q(i))$ is finite.

This is the finiteness theorem of M. Artin, SGA 4, Exposé XIV, for the constant coefficients $\mathbb{Z}/q(i)$ (see also J. S. Milne, *Étale Cohomology*, Chapter VI, §2).

Lean: `UpperTheory.Et.etale_finiteness_of_duality` (also `UpperTheory.Et.e4` and `UpperTheory.Et.EtaleTopology.top`, the same statement with the axioms as hypotheses).

### The inputs

The proof uses the following results, which we take as given. Let $k$ and $q$ be as in the theorem, and write $H^n(X)$ for $H^n(X, \mathbb{Z}/q(i))$.

1. *Points.* For an algebraically closed field $\Omega$ with $q$ a unit, $H^0(\operatorname{Spec} \Omega)$ is finite, and $H^0(\operatorname{Spec} \Omega) \to H^0(X)$ is bijective for every connected $X$ over $\Omega$. A proper integral scheme of dimension $0$ over $k$ has finite cohomology in all degrees.
2. *Units and Picard groups.* Let $B$ be a Dedekind domain of finite type over an algebraically closed field $\Omega$, with $q$ a unit in $\Omega$. Then $B^\times / (B^\times)^q$ is finite, and the $q$-torsion subgroup $\operatorname{Pic}(B)[q]$ is finite.
3. *Kummer sequence.* Let $B$ be an algebra over such an $\Omega$. If $B^\times/(B^\times)^q$ and $\operatorname{Pic}(B)[q]$ are finite, then $H^1(\operatorname{Spec} B)$ is finite. The idea is the exact sequence
$$0 \to B^\times / (B^\times)^q \to H^1(\operatorname{Spec} B, \mu_q) \to \operatorname{Pic}(B)[q] \to 0,$$
which comes from the Kummer sequence $0 \to \mu_q \to \mathbb{G}_m \xrightarrow{q} \mathbb{G}_m \to 0$ and the isomorphism $H^1(\operatorname{Spec} B, \mathbb{G}_m) \cong \operatorname{Pic}(B)$ (axiom B6, Hilbert 90 in the form of Grothendieck, see J. S. Milne, *Étale Cohomology*, Chapter III, Proposition 4.9).
4. *Curves.* A *curve* over $\Omega$ is an integral scheme $C$, proper and smooth of relative dimension $1$ over $\Omega$. Assume that $H^1(\operatorname{Spec} B)$ is finite for every $B$ as in 2. Then $H^1(C)$ and $H^2(C)$ are finite, and $H^m(C) = 0$ for $m \geq 3$.
5. *Killing classes.* Let $C$ be a curve, $m > 0$, and $H^m(C)$ finite. Then there is a surjective map $\gamma : C' \to C$ from a curve $C'$ with $\gamma^* = 0$ on $H^m(C)$.
6. *Descent and the spectral sequence.* Let $f : Y \to X$ be proper and surjective, with $X$ proper over $k$. Assume that $H^m(Z)$ is finite for all proper $Z \to X$ and all $m < n$. Then the kernel of $f^* : H^n(X) \to H^n(Y)$ is finite. The idea: $f$ is a map of cohomological descent, and the descent spectral sequence bounds the kernel by groups $H^m$ with $m < n$ of the fibre products $Y \times_X \cdots \times_X Y$.
7. *Components.* Let $X$ be proper over $k$, and assume that $H^n(Z)$ is finite for every integral closed subscheme $Z \subseteq X$. Then there is a proper surjective $Y \to X$ with $H^n(Y)$ finite.
8. *Fibration by curves.* Let $X$ be integral and proper over $k$ of dimension $d > 0$. Then there are an algebraically closed field $\Omega \supseteq k$ and a curve $C_0$ over $\Omega$ with this property. For all surjective maps of curves $C_2 \to C_1 \to C_0$ there are: an integral proper $k$-scheme $B$ with $\dim B < d$, a closed subscheme $W \subseteq B$ with complement $V$, proper maps $Y_2 \to Y_1 \to Y_0 \to B$ that are smooth over $V$, a map $h : Y_0 \to X$ such that $Y_2 \to X$ is proper and surjective, with $\dim (Y_0 \times_B W) < d$, and a geometric point $s : \operatorname{Spec} \Omega \to V$ whose fibres are $C_0$, $C_1$ and $C_2$.
9. *Spreading out.* In the situation of 8, properties of the fibres at $s$ pass to the fibres at every strictly henselian point $t$ of $V$: vanishing of $H^m$, the vanishing of a pullback map, and a bijection on $H^0$.
10. *Classes from the base.* In the situation of 8, assume that at every strictly henselian point $t$ of $V$ the fibre of $Y_0$ has $H^m = 0$ for $m \geq 3$, the map $Y_1 \to Y_0$ kills $H^2$ of the fibres, the map $Y_2 \to Y_1$ kills $H^1$ of the fibres, and the pullback from $H^0$ of the strictly henselian point to $H^0$ of the fibre of $Y_2$ is bijective. Then for each class $a \in H^n(Y_0)$ that vanishes on $Y_0 \times_B W$, the pullback of $a$ to $Y_2$ comes from a class $b \in H^n(B)$.

Results 9 and 10 are where proper base change enters. The geometric idea of 10 is the Leray spectral sequence of $Y_0 \to B$ over $V$: after the two covers, the classes of positive degree along the fibres die, and what is left comes from the base.

### The proof

We also need a lemma on groups. Let $\varphi : A \to C$, $r : A \to D$ and $\psi : E \to C$ be homomorphisms of abelian groups with $D$ and $E$ finite and $\ker \varphi$ finite. Assume that for each $a \in \ker r$ there is $b \in E$ with $\psi(b) = \varphi(a)$. Then $A$ is finite. Indeed, $A / \ker r$ embeds in $D$. The map $\varphi$ sends $\ker r$ into $\psi(E)$, which is finite, and its kernel on $\ker r$ is finite. So $\ker r$ is finite, and so is $A$.

*Proof of the theorem.* Fix $q$, $i$ and $k$. We prove by induction on $N \geq 0$ that $H^m(X)$ is finite for all proper $X$ over $k$ and all $m < N$. For $N = 0$ this holds because $H^m = 0$ for $m < 0$ by axiom A9.

Assume the claim for $N = n$. We show that $H^n(X)$ is finite for all proper $X$, by induction on $\dim X$. First, by input 6 and the claim for degrees below $n$, every proper surjective $f : Y \to X$ has $\ker(f^* : H^n(X) \to H^n(Y))$ finite.

*$X$ integral.* If $\dim X = 0$, input 1 applies. Let $\dim X = d > 0$, and take $\Omega$ and $C_0$ from input 8. By inputs 2, 3 and 4, $H^1(C)$ and $H^2(C)$ are finite for every curve $C$ over $\Omega$, and $H^m(C) = 0$ for $m \geq 3$. By input 5, there is a cover $C_1 \to C_0$ that kills $H^2(C_0)$, and a cover $C_2 \to C_1$ that kills $H^1(C_1)$. Input 8 gives $B$, $W$, $Y_0$, $Y_1$, $Y_2$ and $h$ for these covers. By input 9, the hypotheses of input 10 hold at every strictly henselian point of $V$. The $H^0$ condition there comes from input 1, since $C_2$ is connected.

Now apply the lemma on groups with $A = H^n(X)$, $C = H^n(Y_2)$, $D = H^n(Y_0 \times_B W)$ and $E = H^n(B)$. The groups $D$ and $E$ are finite by the induction on dimension, since $\dim B < d$ and $\dim(Y_0 \times_B W) < d$. The kernel of $\varphi : H^n(X) \to H^n(Y_2)$ is finite, since $Y_2 \to X$ is proper and surjective. If $a \in H^n(X)$ vanishes on $Y_0 \times_B W$, then $h^* a$ satisfies the hypothesis of input 10, so its pullback to $Y_2$ comes from $H^n(B)$. So $H^n(X)$ is finite.

*$X$ arbitrary.* Every integral closed subscheme $Z$ of $X$ is proper over $k$ with $\dim Z \leq \dim X$, so $H^n(Z)$ is finite by the integral case. Input 7 gives a proper surjective $f : Y \to X$ with $H^n(Y)$ finite. Since $\ker f^*$ is finite, $H^n(X)$ is finite.

This proves the claim for $N = n + 1$. $\square$

**Remark 3.7.2 (Formalization).** The induction takes the axioms except A6, B6 and E4 as one record of 27 hypotheses (A1 to A5, A7 to A11, B1 to B5, B7, C1 to C5, D1 to D3, E1 to E3); this is `UpperTheory.Et.EtaleTopology.top`. Its hypothesis B6 is a hidden section variable ([EtaleTopology.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleTopology.lean#L130)), used once for the Kummer sequence (line 166). So `UpperTheory.Et.e4` is an implication from the 27 hypotheses to E4 ([E4.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/E4.lean#L5)), and only `UpperTheory.Et.etale_finiteness_of_duality` is unconditional: it fills the record with theorems, among them [Corollary 3.1.7](/entry/etale-duality-trace-isomorphism/) for D2 and [Theorem 3.6.1](/entry/proper-base-change/) for E2. Its name is misleading: it does not use duality, and E8 is not among its hypotheses. Its instance $q \neq 0$ is redundant. The ten inputs are separate results, which we checked from their statements ([H0TwistOverClosedField.lean](lean:Development/EtaleCohomology/EtaleSheaves/H0TwistOverClosedField.lean#L25), lines 25 to 95); all except the units and the fibration take the whole record. The induction is at line 114.

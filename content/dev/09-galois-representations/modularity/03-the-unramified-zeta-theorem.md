---
title: The unramified zeta theorem
decls:
  - UpperTheory.V.Z.Kato.Joint.towerEx
  - UpperTheory.V.Z.Kato.Joint.thOp
  - UpperTheory.V.Z.Kato.Joint.kato_global_admissibility_of_admissible
  - UpperTheory.V.Z.Kato.Joint.kato_global_unit_law_of_smoothed_classes
  - UpperTheory.V.Z.Kato.Final.zetaUr
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The unramified zeta theorem

This section proves the unramified zeta theorem: an ordinary representation in normal form that comes from a newform with good ordinary reduction at $l$ has an Euler system class that is unramified away from $l$ and is not ordinary at $l$. This is the input of the [ordinary vanishing theorem](/entry/vanish-ord-l-of-zeta-ur/), which Section 2 applies twice. The proof joins three results: Kato's integral Euler system of zeta classes, the Hodge-Tate law of smoothed zeta classes of Section 4, and an admissible Hecke functional. This section proves the existence of a tower of modular functions, the action of Hecke operators on theta coefficients and the admissible functional, and then joins the parts. The background on [Euler systems and Kato](/learn/galois-cohomology/#euler-systems-and-kato), [modular forms](/learn/automorphic-forms/#modular-forms) and [Iwasawa theory](/learn/galois-cohomology/#iwasawa-theory) is in Volume 1.

### Setting

We keep the notation of Section 2: $l$ is a prime, $\Omega$ an algebraic closure of $\mathbb{Q}$, $\iota \colon \overline{\mathbb{Q}}_l \to \mathbb{C}$ an isomorphism, $\varepsilon$ the cyclotomic character, and $D_A$, $I_A$ the decomposition and inertia groups of a valuation ring $A$ of $\Omega$. A representation $W \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_l)$ in *normal form for $(e, S, A)$* is as in the chapter on Hecke algebras (Section 20 there). We write $a \equiv_n b$ when $|a - b| \leq |l^n|$.

A *tower of modular functions* over $\Omega$, for an embedding $\epsilon \colon \Omega \to \mathbb{C}$, is a field of modular functions of all levels with $q$-expansions over $\Omega$, an action of $\mathrm{GL}_2^+(\mathbb{Q})$ and of $\mathrm{Gal}(\Omega/\mathbb{Q})$, a reciprocity law and the $j$-function, as in [towers of modular functions](/entry/tower-exists/). For a tower $X$, levels $N$ and weights $w$ there are the $l$-adic Kummer modules with bases $X.B(N, l, w)$, with Hecke operators $T_q$, $U_l$ and diamond operators $\langle d\rangle$.

**Definition 8.3.1 (Ordinary newform source).** Let $e \geq 0$, let $A$ be a valuation ring over $l$ and let $g$ be a newform of weight $2e + 1$. Then $g$ is an *unramified source* for $W$ at $A$ if $l$ does not divide the level of $g$, $|\iota^{-1} a_l(g)| = 1$, and there is a character $\chi$ that kills $\mu_l$ such that $g$ is attached to $\varepsilon^{-e}(\det W)^{-1}\chi \otimes W$ and, for $s \in I_A$,
$$W(s)_{22}\, \varepsilon(s)^{e} \det W(s)^{-1} \chi(s) = 1.$$

**Definition 8.3.2 (Euler system class unramified away from $l$).** The representation $W$ has an *unramified Euler system class at $A$* if there are a coefficient ring $\mathcal{O}$ that contains the entries of $W$, a cocycle $y$ for $W$ with values in $\mathcal{O}^2$ and a finite set $S'$ of places such that $y$ is unramified away from $l$, $y$ does not satisfy the Greenberg condition at $A$, and $y$ has a tame class at $(w, n, \psi)$ for each $n \geq 1$, each place $w \notin S'$ with $l^n \mid Nw - 1$ and each surjective $\psi \colon G_{\mathbb{Q}} \to \mathbb{Z}/l^n$ that kills $\mu_{Nw}$. Tame classes are defined in [gluing an Euler system class](/entry/middle-glue2/).

### Towers and theta coefficients

**Theorem 8.3.3 (Towers exist).** For each algebraic closure $\Omega$ of $\mathbb{Q}$ and each embedding $\epsilon \colon \Omega \to \mathbb{C}$ there is a tower of modular functions over $\Omega$ for $\epsilon$.

Lean: `UpperTheory.V.Z.Kato.Joint.towerEx`.

*Proof.* The [tower theorem with algebraic coefficients](/entry/exists-modular-function-tower-algebraic-coefficients/) gives a tower with one more property, on the algebraicity of the coefficients. We keep the tower and drop that property. $\square$

Let $X$ be a tower, $A$ a valuation ring of $\Omega$, $N \geq 1$, $w \geq 0$ and $j \colon \Omega \to \overline{\mathbb{Q}}_l$ an embedding. The data are *standard* if $l$ is not a unit in $A$, $l \neq 2$, $l \nmid N$, $N \geq 5$, $w$ is odd and $|j(x)| \leq 1$ for $x \in A$. For an element $b$ of the Kummer module and $n \geq 0$, the *theta coefficients* $\vartheta_n(b) = (\vartheta_n(b)_i)_{i \geq 0}$ are the images under $j$ of the $q$-expansion coefficients of the theta lattice of $b$ modulo $l^n$, as in the chapter on [Hecke algebras](/entry/th-n-hecke/).

The *admitted letters* for $(N, l)$ are $T_q$ for primes $q \nmid lN$, $U_l$, and $\langle d\rangle$ for $d$ prime to $N$. For a weight $k$ and $\chi \colon \mathbb{N} \to \mathbb{Z}_l$, the *formal operators* on sequences are
$$\begin{aligned} (T_q a)_i &= a_{qi} + \chi(q)\, q^{k-1} a_{i/q}, \\ (U_l a)_i &= a_{li}, \qquad (\langle d\rangle a)_i = \chi(d)\, a_i, \end{aligned}$$
with $a_{i/q} = 0$ when $q \nmid i$. An element $b$ is in the *$\chi$-part* of weight $w$ if $b \in X.B(N, l, w)$ and $\langle d\rangle b = \chi(d)\, b$ for $d$ prime to $N$.

**Theorem 8.3.4 (Hecke operators on theta coefficients).** Let $(X, A, N, w, j)$ be standard and $\chi \colon \mathbb{N} \to \mathbb{Z}_l$. Let $n \geq 0$, let $T$ be an admitted letter and $b$ in the $\chi$-part of weight $w$. Then for each $i$,
$$\vartheta_n(T b)_i \equiv_n \bigl(T\, \vartheta_n(b)\bigr)_i,$$
where on the right $T$ is the formal operator of weight $w + 2$.

Lean: `UpperTheory.V.Z.Kato.Joint.thOp`.

*Proof.* The diamond operators act on the theta lattice of $b$ through $\chi$, and the cusp functional modulo $l^n$ commutes with the Hecke and diamond operators; both facts are in the chapter on [Hecke algebras](/entry/th-n-hecke/). We treat the three kinds of letters.

For $T_q$, the $q$-expansion of $T_q b$ is $U_q$ of the expansion of $b$ plus $q^{w+1}$ times $V_q$ of the expansion of $\langle q\rangle b$. Here $U_q$ takes the coefficient of $q^{qi}$, and $V_q$ moves the coefficient of $q^{i}$ to $q^{qi}$. Since $b$ is in the $\chi$-part, the second term has coefficient $\chi(q)\, q^{w+1} a_{i/q}$ modulo $l^n$ when $q \mid i$. When $q \nmid i$ the coefficient at $i/q$ of a lattice expansion is $0$. The images under $j$ keep the congruences, since $|j| \leq 1$ on $A$. For $U_l$ only the first term occurs, and for $\langle d\rangle$ the action is the scalar $\chi(d)$. $\square$

### The admissible functional

We take as given the *admissible projection statement*: for standard data, a newform $g_N$ of weight $2e + 1$, a representation $\rho$ of the form $\rho_K(W, e, \psi)$ that is upper triangular on $D_A$, with lower right entry $1$ on $I_A$ and upper left entry a power of the cyclotomic character on an open subgroup of $I_A$, and an evaluation of the admitted letters by the Hecke eigenvalues of $g_N$, each admissible polynomial in the letters with value $1$ cuts out a projection of the Kummer module onto copies of $\rho$, and each finite functional that is a Hecke eigenfunctional modulo $l^{n - c_2}$ on the $\chi$-part factors through this projection. A second form of this statement, with generated Hecke algebras, gives the first.

**Theorem 8.3.5 (Admissible functional).** Assume the admissible projection statement. Let $W$ be in normal form for $(e, S, A)$ and let $g$ be an unramified source for $W$ at $A$ with character $\chi_g$, where $\chi_g(s) = \psi_0(\varepsilon(s) \bmod l)$. Let $j \colon \Omega \to \overline{\mathbb{Q}}_l$ with $A = \{x : |j(x)| \leq 1\}$, let $X$ be a tower, $N \geq 5$ with the level of $g$ dividing $N$ and $l \nmid N$, and $\chi$ a Dirichlet character modulo $N$ that agrees with the character of $g$. Let $\alpha$ be a unit root of
$$X^2 - a_l(g) X + \chi(l)\, l^{2e},$$
with an Eisenstein eigenfunctional of [ordinary Eisenstein type](/entry/ordinary-eisenstein-eigenfunctional-exists/) for $(g, \alpha)$, given by $B$ and $c$. Then for each coefficient ring $\mathcal{O}_0$ there are a projection $\mathrm{pr}$ of the Kummer module to $\overline{\mathbb{Q}}_l^2$, a coefficient ring $\mathcal{O} \supseteq \mathcal{O}_0$, a character $\chi_d$ with values in $\mathbb{Z}_l$, a linear functional $\lambda$ on sequences and $\kappa \neq 0$ such that:

1. $\mathrm{pr}$ is $\mathbb{Z}_l$-linear and has values in $\mathcal{O}^2$ on the basis of weight $2e - 1$;
2. $\mathrm{pr}(s b) = \rho_K(W, e, \psi_0)(s)\, \mathrm{pr}(b)$ for each $s$;
3. $\mathrm{pr}(T_q b) = \iota^{-1} a_q(g)\, \mathrm{pr}(b)$ for $q \nmid lN$, the diamond operators act by scalars, and $\mathrm{pr}(U_l b) = \iota^{-1}\alpha\, \mathrm{pr}(b)$;
4. $\iota\chi_d = \chi$ on integers prime to $N$, and $\mathrm{pr}(\langle d\rangle b) = \chi_d(d)\, \mathrm{pr}(b)$;
5. $\lambda$ satisfies the Frobenius relation for $(X, A, N, 2e - 1, \chi_d, j, \mathrm{pr}, \mathcal{O})$;
6. for each modular form with coefficients $\iota(a_i)$ of weight $2e + 1$, level $Nl$ and character $\chi$, $\lambda(a) = \kappa\, \iota^{-1}\Lambda(a)$, where $\Lambda$ is the Eisenstein functional.

Lean: `UpperTheory.V.Z.Kato.Joint.kato_global_admissibility_of_admissible`.

*Proof.* We have the [Hecke projector onto the newform part](/entry/hecke-projector-newform-galois-image/) of the Kummer module, with its Galois image, and the ordinary triangular shape of the untwisted representation $\rho_K$. With Theorem (Hecke operators on theta coefficients), the linearity of theta coefficients, the stability of the $\chi$-part under the letters, the eigenvalues of the Eisenstein functional and local facts at $l$, the admissible projection statement gives the projection and the functional. $\square$

### Joining the halves

An *Iwasawa datum* for $W$ at $A$ is a coefficient ring $\mathcal{O}$, an Euler system class $y$ for $W$, $\mathcal{O}$ and a finite set $S'$, a character $\nu$ that is trivial on $I_A$, a family $\chi_r$ of functions on $(\mathbb{Z}/l^r)^\times$ and an Iwasawa system $Z_r$ for $\nu$ that is linked to $y$ with weight $e$, as in [gluing an Euler system class](/entry/middle-glue2/), together with a *Coleman condition*: the value of $\nu$ on a Frobenius element at $A$ is a unit, and the Hodge-Tate sums of $Z$ are congruent modulo $l^{m - c_0}$ to a fixed unit multiple of character sums of a power series with coefficients in $\mathcal{O}$.

**Theorem 8.3.6 (Existence of Iwasawa data).** Assume Kato's integrality statement for Euler systems, the Hodge-Tate law of smoothed zeta classes and the second form of the admissible projection statement. Let $e \geq 0$, let $W$ be in normal form for $(e, S, A)$ and let $g$ be an unramified source for $W$ at $A$. Then $W$ has an Iwasawa datum at $A$ with the Coleman condition.

Lean: `UpperTheory.V.Z.Kato.Joint.kato_global_unit_law_of_smoothed_classes`.

*Proof.* The gluing theorem joins Kato's integral system, the Hodge-Tate law and the admissible functional of Theorem (Admissible functional). Its other inputs are Theorem (Towers exist), the [ordinary Eisenstein eigenfunctional](/entry/ordinary-eisenstein-eigenfunctional-exists/), and a list of facts on measures, the $j$-function, coefficient bounds, Frobenius at $l$, the determinant on inertia, smoothing and averages. $\square$

**Theorem 8.3.7 (Unramified zeta theorem).** Let $l$ be a prime, $e \geq 0$, $S$ a finite set of places and $A$ a valuation ring of $\Omega$. Let $W$ be in normal form for $(e, S, A)$, and let $g$ be a newform of weight $2e + 1$ that is an unramified source for $W$ at $A$. Then $W$ has an unramified Euler system class at $A$.

Lean: `UpperTheory.V.Z.Kato.Final.zetaUr`.

*Proof.* The theorem has two halves. The first half is Theorem (Existence of Iwasawa data). Its inputs are [Kato's integrality](/entry/kato-euler-system-integrality/), the [Hodge-Tate law of smoothed zeta classes](/entry/smoothed-zeta-class-hodge-tate-law/) of Section 4 and the second form of the admissible projection statement, which follows from the existence of a nonvanishing admissible Hecke projection. The second half is the theorem of [Coleman power series and nonvanishing on inertia](/entry/p-locu/): under the Coleman condition, the Euler system class $y$ of an Iwasawa datum is nonzero on $I_A$. Then $y$ is unramified away from $l$ and is not ordinary at $A$, so it does not satisfy the Greenberg condition, and $W$ has an unramified Euler system class at $A$. $\square$

**Remark 8.3.8 (Formalization).** The unramified zeta theorem gives the Coleman condition as `_`, so Lean infers `GlobalTheory.KZ.Pin7` from the two halves ([ZetaUr.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/UnramifiedZeta/ZetaUr.lean#L9)); the step from the halves is `GlobalTheory.KZ.zetaUr_of_halves2`. The name of the theorem on Iwasawa data says "unit law", but its conclusion is the existence of the data ([KatoGlobalUnitLawOfSmoothedClasses.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/KatoGlobalUnitLawOfSmoothedClasses.lean#L8)). The second form `AdmTop2` of the admissible projection statement enters only through `admissibleHeckeAlgebra_of_generated`, which turns it into `AdmTop`, and the theorem on the admissible functional is a single application of `admissibleFunctional_of_projection` ([KatoGlobalAdmissibilityOfAdmissible.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/KatoGlobalAdmissibilityOfAdmissible.lean#L35)). We summarize `AdmTop`, `AdmFR`, the Frobenius relation `IsLamFR` and the Coleman condition `Pin7` in words and do not unfold them in full. The tower theorem discards the second component of the tower theorem with algebraic coefficients ([TowerEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/TowerEx.lean#L9)). The statement on theta coefficients is the definition `ThOp` ([ChiQuadAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/ChiQuadAlt.lean#L50)), proved in [CgAppr.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/CgAppr.lean#L120).

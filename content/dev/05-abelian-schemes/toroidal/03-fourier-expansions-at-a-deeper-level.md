---
title: Fourier expansions at a deeper level
decls:
  - GlobalTheory.T.unitary_classicalTraits_fourierTerms_all_levels
  - GlobalTheory.UPoinc.four_of_classical
  - GlobalTheory.T.unitary_fourierClassSums_deeper_level
  - GlobalTheory.UPoinc.uclassSums_deeper
  - GlobalTheory.T.unitary_classSums_deeper_level_integralClosure
  - GlobalTheory.UPoinc.ClassCore.classSums_core
  - GlobalTheory.T.unitary_classSums_deeper_level_geometric_core
  - GlobalTheory.UPoinc.UCore.classSums_core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Fourier expansions at a deeper level

The boundary ideal of Section 4 is built on a finite normal cover of the minimal compactification on which theta constants are functions. This section proves that, at a point $z_1$ of the cover, these theta constants have Fourier expansions at every deeper level along the $\ell$-adic boundary traits through $z_1$. The terms are bounded by the monodromy form of the trait, and the Galois group of the deeper level acts through the lattice. We collect the traits in a *Fourier presystem*, and we prove that it has class sums at each deeper level, and then orbit sums. [The theorem on approximating Poincaré series](/entry/exists-u-approx-at/) of Section 4 uses the last result. We use the notation of Sections 1 and 2. For a prime $\ell$, we let $\bar{\mathbb{Q}}_\ell$ be an algebraic closure of $\mathbb{Q}_\ell$ with its norm, $\mathcal{O}_\ell$ its valuation ring, $c_\ell$ the closed point of $\operatorname{Spec} \mathcal{O}_\ell$ and $g_\ell : \operatorname{Spec} \bar{\mathbb{Q}}_\ell \to \operatorname{Spec} \mathcal{O}_\ell$ the generic point. For an abelian group $X$, we write $x \equiv x' \pmod N$ if $x - x' \in N X$.

**Definition 7.3.1 (Boundary trait).** Let $X$ be a moduli scheme for $D$ and $l$, and $F$ a coefficient field. A *boundary trait* $T$ of $X_F$ consists of a complete discrete valuation ring $V$ with uniformizer $\varpi$, a point $y_T : \operatorname{Spec} \operatorname{Frac} V \to X_F$, a semi-abelian datum on $V$ that extends the universal datum at $y_T$, a uniformization $P$ of this datum along the maximal ideal with character lattice $X_T$, and a level form $\beta_T \in \operatorname{levelForms}(H, 1)$ on $X_T$, such that the periods of $P$ are monomial in $\varpi$ with exponent $\beta_T$.

Lean: `GlobalTheory.UPoinc.UTrait`.

These are the traits of the order along boundary traits in Section 2.

**Definition 7.3.2 (Theta setup).** Let $C$ be a minimal compactification of $X_F$. A *theta setup* $X_1$ for $C$ consists of:

1. a ring $o_1$ and a field $\Omega_1$ that form an arithmetic base, and a theta system $S$ over them: a genus $g$, a level $L = r_S N_S$ with $N_S \ge 2$ that is a unit in $o_1$, and theta constants $\theta_a$ for $a \in (\mathbb{Z}/L)^{2g}$, not all zero, in a finitely generated $o_1$-algebra $R \subset \Omega_1$ with fraction field $\Omega_1$;
2. a real point of $S$, which gives a polarized abelian variety over $R$, and a size condition on $S$, which gives $L \ge 3$;
3. a map $u$ from the spectrum of a subalgebra $R' \supset R$ of $\Omega_1$ to $X_F$, along which the universal abelian scheme pulls back to this abelian variety, and which sends generic points to generic points;
4. a model $M$ over $(o_1, \Omega_1)$ with a normal scheme $Z_M$ and a point $\mathrm{pt}_M : \operatorname{Spec} \Omega_1 \to Z_M$, and a finite map $\pi : Z_M \to Z_C$ with $\pi \circ \mathrm{pt}_M = i \circ u$ on $\operatorname{Spec} \Omega_1$.

Lean: `GlobalTheory.UPoinc.USetup` (also `GlobalTheory.ZH.ThetaSys`).

**Definition 7.3.3 ($\ell$-adic boundary trait).** Let $X_1$ be a theta setup, $\ell$ a prime and $z_1 \in Z_M$. An *$\ell$-adic boundary trait* $t$ through $z_1$ consists of a map $y_t : \operatorname{Spec} \mathcal{O}_\ell \to Z_M$ with $y_t(c_\ell) = z_1$, a boundary trait $T$, and a ring map $\iota : \operatorname{Frac} V \to \bar{\mathbb{Q}}_\ell$ with $|\iota(x)| \le 1$ exactly when $x \in V$, such that $\pi \circ y_t \circ g_\ell = i \circ y_T \circ \operatorname{Spec} \iota$. Its *scale* is $\mathrm{sc}_t = -\log |\iota(\varpi)|$, and its *value map* $\mathrm{val}_t : \mathcal{O}_{Z_M, z_1} \to \bar{\mathbb{Q}}_\ell$ sends a germ to its value at the point $y_t \circ g_\ell$.

Lean: `GlobalTheory.UPoinc.UCTrait` (also `GlobalTheory.UPoinc.UCTrait.sc`, `GlobalTheory.UPoinc.UCTrait.val`).

**Definition 7.3.4 (Fourier presystem).** Let $m \in \mathbb{N}$, $\ell$ a prime and $A$ a local ring. A *Fourier presystem* $\Phi$ of rank $m$ over $A$ consists of a set $Y$ and, for each $y \in Y$:

1. a ring map $\mathrm{ev}_y : A \to \bar{\mathbb{Q}}_\ell$ with $|\mathrm{ev}_y(a)| \le 1$ for all $a$ and $|\mathrm{ev}_y(a)| < 1$ on the maximal ideal;
2. a finitely generated projective $\mathcal{O}_E$-module $X_y$ of rank at most $m$ that is free of finite rank over $\mathbb{Z}$;
3. a balanced form $\beta_y$ on $X_y$ with $\beta_y(x, x) > 0$ for $x \ne 0$;
4. a scale $\mathrm{sc}_y > 0$.

We write $Q_y(\mu) = \beta_y(\mu, \mu)$. An element $y$ *matches* an $\ell$-adic boundary trait $t$ if $\mathrm{ev}_y = \mathrm{val}_t$ and there is an $\mathcal{O}_E$-linear isomorphism $e : X_y \to X_T$ with $\mathrm{sc}_y \beta_y(a, b) = \mathrm{sc}_t \beta_T(e a, e b)$. We say that $\Phi$ *covers* $z_1$ if each trait through $z_1$ is matched by some $y$.

Lean: `GlobalTheory.Poinc.FPre` (also `GlobalTheory.UPoinc.UMatches`).

**Definition 7.3.5 (Fourier expansions and class sums).** Let $\Phi$ be a Fourier presystem over $A$. Let $N_1 \mid N$, $y_0 \in Y$, and let $k_y : X_{y_0} \to X_y$ be $\mathbb{Z}$-linear maps.

1. A family $t_y(\mu, \kappa) \in \bar{\mathbb{Q}}_\ell$, for $\mu \in X_y$ and $\kappa$ in a set $Q$, is a family of *Fourier terms* if $|t_y(\mu, \kappa)| \le \exp(-\mathrm{sc}_y Q_y(\mu))$, with equality for some $\kappa$ for each $y$ and $\mu$.
2. $k_y$ is *unimodular modulo $N$* if $k_y(cx) \equiv c\, k_y(x) \pmod N$ for $c \in \mathcal{O}_E$, and $N \mid \det(\varepsilon \circ k_y) - 1$ for some isomorphism $\varepsilon : X_y \to X_{y_0}$. The *orbit* of a tuple $a$ in $X_{y_0}$ is the set of tuples $\mu$ in $X_y$ with $\mu_i \equiv k_y(\gamma a_i) \pmod N$ for some $\mathbb{Z}$-linear $\gamma$ on $X_{y_0}$ that is $\mathcal{O}_E$-linear modulo $N$, with $N \mid \det \gamma - 1$ and $\gamma \equiv 1 \pmod {N_1}$.
3. $\Phi$ has *orbit sums* for $t$ if for each tuple $a_1, \dots, a_n$ in $X_{y_0}$, labels $c_1, \dots, c_n$ and $e \in \mathbb{N}$ there is $f \in A$ such that for each $y$ there is $h$ in the maximal ideal with this property: for each $\varepsilon > 0$ there is a finite set $S$ in the orbit of $a$, outside of which $\exp(-\mathrm{sc}_y \sum_i Q_y(\mu_i)) < \varepsilon$, and with $|\mathrm{ev}_y(f) - \sum_{\mu \in S} \prod_i t_y(\mu_i, c_i)| \le \max(\varepsilon, |\mathrm{ev}_y(h)|^e)$.
4. $\Phi$ has *Fourier expansions at level $N_1$* if for each $y_0$ and $N_0$ there are $N \ge N_0$ with $N_1 \mid N$, maps $k_y$ unimodular modulo $N$ with $k_{y_0} = \mathrm{id}$, and Fourier terms $t$ for which $\Phi$ has orbit sums.
5. Let $B$ be an $A$-algebra and $\mathfrak{z}$ an ideal of $B$. $\Phi$ has *class sums* for $t$ over $(B, \mathfrak{z})$ if there are ring maps $\mathrm{ev}'_y : B \to \bar{\mathbb{Q}}_\ell$ that extend $\mathrm{ev}_y$, with norms at most $1$ and less than $1$ on $\mathfrak{z}$, and a map $f : X_{y_0} \times Q \to B$ such that: $f(c, \kappa)$ depends only on $c$ modulo $N$; for each $y$, $c$ and $\kappa$, the sums $\sum_{\mu \in S} t_y(\mu, \kappa)$ over finite sets $S$ of $\mu \equiv k_y(c) \pmod N$ converge to $\mathrm{ev}'_y(f(c, \kappa))$; and for each $A$-automorphism $\sigma$ of $B$ with $\sigma^{-1}(\mathfrak{z}) = \mathfrak{z}$ there is $\gamma$ as in the orbit with $\sigma(f(c, \kappa)) = f(\gamma c, \kappa)$.

Lean: `GlobalTheory.Poinc.FPre.Four` (also `GlobalTheory.Poinc.FPre.IsTerms`, `GlobalTheory.Poinc.IsUnimodMod`, `GlobalTheory.Poinc.orbit`, `GlobalTheory.Poinc.FPre.OrbitSums`, `GlobalTheory.Poinc.FPre.ClassSums`).

In the theorems below, $X_1$ is a theta setup for a minimal compactification $C$ of $X_F$ with $p + q \ge 1$, $\ell$ is a prime, $z_1 \in Z_M$, $A = \mathcal{O}_{Z_M, z_1}$, and $\Phi$ is a Fourier presystem of rank $\min(p, q)$ over $A$ in which each $y$ matches some $\ell$-adic boundary trait through $z_1$.

**Theorem 7.3.6 (Class sums at a deeper level).** For each $y_0 \in Y$ and $N_0$ there are $N \ge N_0$ with $L \mid N$ and a finite Galois extension $\Omega_2$ of $\Omega_1$ with this property. Let $B$ be the integral closure of $A$ in $\Omega_2$, $\mathfrak{z}$ a maximal ideal of $B$, and $\mathrm{ev}'_y : B \to \bar{\mathbb{Q}}_\ell$ ring maps that extend $\mathrm{ev}_y$, with norms at most $1$ and less than $1$ on $\mathfrak{z}$. Then there are $\mathcal{O}_E$-linear isomorphisms $k_y : X_{y_0} \to X_y$ with $k_{y_0} = \mathrm{id}$, a set $Q$ and a map $F : X_{y_0} \times Q \to B$ such that:

1. $F(c, \kappa)$ depends only on $c$ modulo $N$;
2. if $\mu \equiv k_y(c) \pmod N$ and $Q_y(\mu)$ is least in the class of $\mu$, then $|\mathrm{ev}'_y F(c, \kappa)| \le \exp(-\mathrm{sc}_y Q_y(\mu)/2)$;
3. if $\mu$ is the only element of least $Q_y$ in its class, there are $c \equiv k_y^{-1}(\mu)$ and $\kappa$ with equality in 2;
4. for each $A$-automorphism $\sigma$ of $B$ with $\sigma^{-1}(\mathfrak{z}) = \mathfrak{z}$ there is an $\mathcal{O}_E$-linear automorphism $\gamma$ of $X_{y_0}$ with $N \mid \det \gamma - 1$, $\gamma \equiv 1 \pmod L$ and $\sigma(F(c, \kappa)) = F(\gamma c, \kappa)$.

Lean: `GlobalTheory.UPoinc.UCore.classSums_core` (also `GlobalTheory.T.unitary_classSums_deeper_level_geometric_core`, a second name).

*Proof.* For each $y$ choose a trait $t_y$ that $y$ matches, with isomorphism $e_y : X_y \to X_{T_y}$. There is a deeper theta setup $X_2$ whose level $N$ is at least $N_0$ and divisible by $L$, whose field $\Omega_2$ is finite Galois over $\Omega_1$, with a finite map $Z_2 \to Z_M$; we tie the theta groups of the two levels by a pair of witnesses. The maximal ideal $\mathfrak{z}$ gives a point $z_2$ of $Z_2$ over $z_1$. Each $y_{t_y}$ lifts to $\operatorname{Spec} \mathcal{O}_\ell \to Z_2$, and since $\mathrm{ev}'_y$ is less than $1$ on $\mathfrak{z}$, the closed point goes to $z_2$. So $t_y$ lifts to a trait of $X_2$ through $z_2$.

Each $t_y$ has a labelling of $(\mathbb{Z}/L)^{2g}$ by $X_{T_y}/L$, which extends to a compatible labelling at level $N$. The labelled lattices of the lifted traits are isomorphic by maps $d_y$ that respect labels, and we put $k_y = e_y^{-1} d_y e_{y_0}$. The theta constants of $X_2$ give elements $f(a, \kappa)$ of $\Omega_2$, integral over $A$, indexed by labels $a$ and a set $Q$, with Fourier terms along each trait. The labelling of $t_{y_0}$ is onto; we choose a label $a(x)$ for each $x$ and put $F(c, \kappa) = f(a(e_{y_0} c), \kappa)$. Property 1 holds because $f$ depends only on the class of the label. Properties 2 and 3 bound the limits of class sums of Fourier terms by their least term, and by a unique least term.

For property 4, $\sigma$ extends to an automorphism of $\Omega_2$, which gives an automorphism $s$ of $Z_2$ over $Z_M$ that fixes $z_2$. Its action on labels and the lift of $t_{y_0}$ followed by $s$ give a second labelled lattice and an isomorphism $g$; we put $\gamma = e_{y_0}^{-1} g\, e_{y_0}$. The compatibility of labels at the two levels forces $\gamma \equiv 1 \pmod L$. As $L \ge 3$, $\det \gamma$ is a unit congruent to $1$ modulo $L$, so it is $1$ and $N \mid \det \gamma - 1$. The Galois action on theta constants gives $\sigma(F(c, \kappa)) = F(\gamma c, \kappa)$. $\square$

**Theorem 7.3.7 (Class sums over the integral closure).** Let $y_0$, $N_0$, $N$, $\Omega_2$, $B$, $\mathfrak{z}$ and $\mathrm{ev}'_y$ be as in the previous theorem. Then there are $\mathbb{Z}$-linear maps $k_y$, unimodular modulo $N$ with $k_{y_0} = \mathrm{id}$, Fourier terms $t$ on a set $Q'$, and a map $f : X_{y_0} \times Q' \to B$ for which the class sum condition holds with $N_1 = L$.

Lean: `GlobalTheory.UPoinc.ClassCore.classSums_core` (also `GlobalTheory.T.unitary_classSums_deeper_level_integralClosure`, a second name).

*Proof.* Take $k_y$, $Q$ and $F$ from the previous theorem; each $k_y$ is unimodular modulo $N$ with $\varepsilon = k_y^{-1}$. As $Q_y$ has values in $\mathbb{N}$, we can choose in each class modulo $N$ an element $\mathrm{sel}_y$ of least $Q_y$. A power of $\iota(\varpi)$ gives $e_{y, \mu}$ with $|e_{y, \mu}| = \exp(-\mathrm{sc}_y Q_y(\mu))$.

Let $Q' = Q \sqcup \{(y, \mu)\}$. For $\kappa \in Q$, let $f(c, \kappa) = F(c, \kappa)^2$, and let $t_y(\nu, \kappa)$ be $\mathrm{ev}'_y(F(k_y^{-1} \nu, \kappa))^2$ at $\nu = \mathrm{sel}_y$ and $0$ elsewhere. For a label $(y, \mu)$, let $f = 0$; if some $w \ne \mu$ in the class of $\mu$ has $Q_y(w) \le Q_y(\mu)$, let $t_y$ be $e_{y, \mu}$ at $\mu$, $-e_{y, \mu}$ at $w$ and $0$ elsewhere, and otherwise $0$.

The bounds on terms follow from property 2 by squaring, and from $Q_y(w) \le Q_y(\mu)$. Equality at $\mu$ comes from property 3 if $\mu$ is the only element of least $Q_y$ in its class, and from the label $(y, \mu)$ otherwise. For $\kappa \in Q$ each class sum has one nonzero term, equal to $\mathrm{ev}'_y(f(c, \kappa))$ by property 1. For $(y, \mu)$ the two terms cancel. The Galois clause follows from property 4. $\square$

**Theorem 7.3.8 (Fourier class sums at a deeper level).** For each $y_0$ and $N_0$ there are $N \ge N_0$ with $L \mid N$, maps $k_y$ unimodular modulo $N$ with $k_{y_0} = \mathrm{id}$, Fourier terms $t$, a domain $B$ finite over $A$ with $A \to B$ injective, finitely many $A$-automorphisms and invariants equal to $A$, and a maximal ideal $\mathfrak{z}$ of $B$, such that $\Phi$ has class sums for $t$ over $(B, \mathfrak{z})$ with $N_1 = L$.

Lean: `GlobalTheory.UPoinc.uclassSums_deeper` (also `GlobalTheory.T.unitary_fourierClassSums_deeper_level`, a second name).

*Proof.* Take $N$ and $\Omega_2$ from the first theorem. The ring $A$ is a noetherian normal domain with fraction field $\Omega_1$, so the integral closure $B$ of $A$ in $\Omega_2$ is finite over $A$, its group of $A$-automorphisms is finite, and its invariants are $A$. We choose a maximal ideal $\mathfrak{z}$ of $B$. Each $\mathrm{ev}_y$ extends to $\mathrm{ev}'_y$ on $B$ with norms at most $1$ and less than $1$ on $\mathfrak{z}$. The previous theorem gives the rest. $\square$

**Theorem 7.3.9 (Fourier expansions at all levels).** $\Phi$ has Fourier expansions at level $L$.

Lean: `GlobalTheory.UPoinc.four_of_classical` (also `GlobalTheory.T.unitary_classicalTraits_fourierTerms_all_levels`, a second name).

*Proof.* Let $y_0$ and $N_0$ be given. The previous theorem for $N_0 + 1$ gives $N \ge N_0 + 1$, $k_y$, $t$, $B$ and $\mathfrak{z}$. Since $A$ is a noetherian normal local domain, $B$ is finite over $A$ with invariants $A$ and $N \ge 1$, the class sums of $t$ give orbit sums for $t$. $\square$

**Remark 7.3.10 (Formalization).** The proofs are in [UnitaryClassSumsDeeperLevelGeometricCore.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryClassSumsDeeperLevelGeometricCore.lean#L42), [UnitaryClassSumsDeeperLevelIntegralClosure.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryClassSumsDeeperLevelIntegralClosure.lean#L298), [UnitaryFourierClassSumsDeeperLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryFourierClassSumsDeeperLevel.lean#L39) and [UnitaryClassicalTraitsFourierTermsAllLevels.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryClassicalTraitsFourierTermsAllLevels.lean#L34). The predicates are in [ClassSums.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ClassSums.lean#L10). The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The prime $\ell$ is `p` in Lean. The predicates of `FPre` take a weight matrix `W` on `s` indices; this chapter uses only `s = 1` and `W = !![1]`, where `qW` is $Q_y$, and we state them only in that case. The proof of the integral closure theorem is `main_of_core` at line 70. Its terms on $Q$ are not the Fourier coefficients of theta constants: each class has one nonzero term, at a least element that `Classical.epsilon` chooses (line 133), and the extra labels $(y, \mu)$ give two terms that cancel. So the class sum and Fourier term conditions of that theorem carry no more information than properties 2 and 3 of the first theorem. The proofs apply lemmas with no entries in this chapter, among them `UDeepP.exists_udeep_proj`, `T.exists_labels_unitaryClassicalTrait`, `T.unitary_trait_labels_extend_to_deeper_level`, `T.exists_linearEquiv_labelledLattices_unitaryTraits`, `T.unitary_thetaFourier_classSums_deeper_integral`, `dvd_det_sub_one_of_congMod_three_le`, `T.extend_integral_padic_evaluation_galois` and `T.approx_orbitSums_of_galois_classSums`. We use only their statements as the proofs apply them. We have not unfolded `ArithBase`, `ThetaSys.Real`, `ThetaSys.Big`, `UOver`, `RatModel`, `ratHull`, `PELUnif`, `IsMonomial`, the labelling `UIsLab` or the label set `HH`.

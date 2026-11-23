---
title: Quasi-logarithms and adapted bases
decls:
  - GlobalTheory.QLogBasis.adapted_basis
  - GlobalTheory.T.exists_adapted_quasiLog_basis_pDivGroup_lieDual
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Quasi-logarithms and adapted bases

This section proves that the formal group of a $p$-divisible group over the ring of integers of an algebraically closed field has a basis of quasi-logarithms of a special form. The first $d$ members are true logarithms, one for each coordinate, and the other members correspond to a basis of the Lie algebra of the dual group. The theorem on period matrices over a frame ([Theorem 5.4.3](/entry/window-matrices/)) starts from such a basis. It lifts the basis to a frame, writes the Frobenius in it, and reads the period matrices off the result. The ring $A_{\inf}$ and the map $\theta$ behind the frames of the later sections are in [period rings](/learn/galois-representations/#period-rings), and power series are in [polynomials and power series](/learn/algebra/#polynomials-and-power-series).

Throughout the chapter $p$ is a prime, $C$ is an algebraically closed field of characteristic $0$, $v$ is a valuation on $C$ with values in $\mathbb{R}_{\geq 0}$, and $O$ is the ring of integers of $v$. We assume that $p$ is not a unit in $O$, that $O$ is a domain and that $O$ is $p$-adically complete. A $p$-divisible group $G$ over $O$ of height $h$ is a system of finite, locally free, commutative and cocommutative Hopf algebras $A_n$ over $O$ of rank $p^{nh}$, with surjective maps $A_{n+1} \to A_n$ whose kernel is the $p^n$-torsion ideal. We write $T_p G$ for its Tate module, $\omega_G$ for its module of invariant differentials, $\mathrm{Lie}(G) = \mathrm{Hom}_O(\omega_G, O)$ for its Lie algebra and $G^\vee$ for its Cartier dual.

**Definition 5.1.1 (Frame).** Let $B$ and $O$ be rings, let $Q$ be a $B$-algebra and let $\theta : B \to O$ be a ring map. The triple $(B, Q, \theta)$ is a *frame* for $p$ if:

1. $\theta$ is surjective, and the map $B \to Q$ is injective;
2. for each $q \in Q$ there are $k \geq 0$ and $b \in B$ with $p^k q = b$ in $Q$;
3. $p$ is a unit in $Q$, and each integer $n$ prime to $p$ is a unit in $B$;
4. if $\theta(x) = 0$, then $x^p = p y$ for some $y$ with $\theta(y) = 0$;
5. if $a \in O$ and $p a = 0$, then $a = 0$;
6. $B$ is $p$-adically complete.

The model case is $B = \mathbb{Z}_p$, $Q = \mathbb{Q}_p$ and $\theta$ the identity. So $Q$ plays the role of $B[1/p]$, and condition 4 says that the kernel of $\theta$ has a weak form of divided powers. In this section we use the frame $(O, E, \mathrm{id})$ for an $O$-algebra $E$, and in the main application $E = C$.

Let $R$ be a ring and $d \geq 0$. For $f$ in $R[[X_1, \ldots, X_d]]$ and a $d$-tuple $\mu = (\mu_1, \ldots, \mu_d)$ of series in two sets of variables $X$ and $Y$, put
$$\delta^1_\mu f = f(\mu(X, Y)) - f(X) - f(Y).$$
Write $\mathrm{lin}(f) \in R^d$ for the vector of coefficients of $X_1, \ldots, X_d$ in $f$. A *formal group law* is a tuple $\mu$ with constant terms $0$, with $\mu(X, 0) = X$, with $\mu(X, Y) = \mu(Y, X)$, and with the associative law. If $B$ maps to $Q$, then a series over $B$ also gives a series over $Q$, and we do not change the name.

**Definition 5.1.2 (Coefficients in an ideal).** Let $N$ be an ideal of $B$ and $f$ a power series over $Q$. We say that $f$ *has coefficients in* $N$ if each coefficient of $f$ is the image of an element of $N$. We say that $f$ has *derivatives in* $N$ if for each multi-index $\alpha$ and each variable $i$, the product $\alpha_i \cdot \mathrm{coeff}_\alpha(f)$ is the image of an element of $N$. When $N = B$ we also say that $f$ is *integral*.

The second condition says that all the first partial derivatives of $f$ have coefficients in $N$.

**Definition 5.1.3 (Quasi-logarithm).** Let $\mu$ be a $d$-tuple of series over $B$ in $X$ and $Y$, and let $N$ be an ideal of $B$. A *quasi-logarithm* for $\mu$ relative to $N$ is a series $f \in Q[[X_1, \ldots, X_d]]$ with constant term $0$, such that each entry of $\mathrm{lin}(f)$ is the image of an element of $N$, and such that $\delta^1_\mu f$ has coefficients in $N$. A family $(e_i)_{i \in I}$, with $I$ finite, is a *basis of quasi-logarithms* for $\mu$ if each $e_i$ is a quasi-logarithm relative to $B$, and if for each quasi-logarithm $f$ relative to $B$ there is exactly one $b \in B^I$ such that $f - \sum_i b_i e_i$ is integral.

**Definition 5.1.4 (Adapted family).** Let $c \geq 0$ and let $e$ be a family indexed by $\{1, \ldots, d\} \sqcup \{1, \ldots, c\}$. Write $e_{(1,i)}$ and $e_{(2,j)}$ for its members. The family is *adapted* for $\theta$ and $\mu$ if for each $i \leq d$ the series $\delta^1_\mu e_{(1,i)}$ has coefficients in $\ker \theta$ and $\mathrm{lin}(e_{(1,i)})$ is the $i$-th unit vector.

A logarithm of a formal group law over a field of characteristic $0$ is a series $\ell$ with $\delta^1_\mu \ell = 0$. Over $\mathbb{Q}_p$, the classical quasi-logarithms of a formal group law over $\mathbb{Z}_p$ are the series $f$ for which $\delta^1_\mu f$ is integral. Integral series are quasi-logarithms in a trivial way, and the definition of a basis counts quasi-logarithms modulo integral series.

A *chart* of dimension $d$ of $G$ consists of $d$ elements $x_{n,1}, \ldots, x_{n,d}$ of each $A_n$, with evaluation maps $O[[X_1, \ldots, X_d]] \to A_n$ that send $X_i$ to $x_{n,i}$ and are surjective, and a formal group law $\mu_c$ over $O$ whose image under the two-variable evaluation is the comultiplication of $x_{n,i}$. The $x_{n,i}$ are topologically nilpotent, they lie in the augmentation ideal, and they are compatible in $n$. The kernels of the evaluations tend to $0$ in a $p$-adic sense.

**Definition 5.1.5 (Lie series).** Let $c$ be a chart of $G$, let $E$ be an $O$-algebra, let $f \in E[[X_1, \ldots, X_d]]$ and let $l \in \mathrm{Lie}(G^\vee)$. For $m \geq 1$ put $D_m f = m f - f([m](X))$, where $[m]$ is the $m$-fold sum for $\mu_c$. The series $f$ is a *Lie series* for $l$ if:

1. for each $n$, the series $D_{p^n} f$ is integral;
2. for each $n$, each $w \in \omega_{G^\vee}$, each point $\varphi$ of the Cartier dual of $A_n$ whose differential is the $n$-th component of $w$, and each series $s$ over $O$ whose image in $E$ is $D_{p^n} f$, the element $l(w) - \varphi(s(x_n))$ is divisible by $p^n$ in $O$.

So the defect $D_{p^n} f$, evaluated on $G[p^n]$, recovers the value of $l$ modulo $p^n$. A true logarithm has defect $0$, and it is a Lie series only for $l = 0$.

**Theorem 5.1.6 (Adapted basis of quasi-logarithms).** Let $p$, $C$, $v$ and $O$ be as above. Let $G$ be a $p$-divisible group over $O$, let $c$ be a chart of $G$ of dimension $d$, and let $E$ be an $O$-algebra such that $(O, E, \mathrm{id})$ is a frame for $p$. Then there are $k \geq 0$, a family $e$ of series in $E[[X_1, \ldots, X_d]]$ indexed by $\{1, \ldots, d\} \sqcup \{1, \ldots, k\}$, and a basis $(l_1, \ldots, l_k)$ of $\mathrm{Lie}(G^\vee)$ over $O$, such that:

1. $e$ is a basis of quasi-logarithms for $\mu_c$;
2. $e$ is adapted for the identity of $O$ and for $\mu_c$;
3. $\delta^1_{\mu_c} e_{(1,i)} = 0$ for each $i \leq d$;
4. $e_{(2,j)}$ is a Lie series for $l_j$, for each $j \leq k$.

Lean: `GlobalTheory.QLogBasis.adapted_basis` (also `GlobalTheory.T.exists_adapted_quasiLog_basis_pDivGroup_lieDual`, a wrapper).

*Proof.* Since $O$ is the ring of integers of a valuation, it is a valuation ring, and so it is local. We take as given that $\omega_{G^\vee}$ is a finite projective $O$-module. A finite projective module over a local ring is free, so $\omega_{G^\vee}$ is free of finite rank, and so is its dual $\mathrm{Lie}(G^\vee)$. Let $k$ be the rank and let $(l_1, \ldots, l_k)$ be a basis.

1. *Lie series exist.* Let $M \subseteq \mathrm{Lie}(G^\vee)$ be the set of $l$ for which there is a quasi-logarithm $f$ relative to $O$ that is a Lie series for $l$. The zero series is a Lie series for $0$. If $f_1$ is a Lie series for $l_1$ and $f_2$ for $l_2$, then $f_1 + a f_2$ is a Lie series for $l_1 + a l_2$, since both conditions are linear in the pair $(f, l)$. So $M$ is a submodule. We take as given that each $x \in \mathrm{Lie}(G^\vee)$ has the form $l' + p l''$ with $l' \in M$. So $\mathrm{Lie}(G^\vee) = M + p\,\mathrm{Lie}(G^\vee)$. The element $p$ is not a unit, so it lies in the maximal ideal, which is the Jacobson radical. The module $\mathrm{Lie}(G^\vee)$ is finitely generated, so Nakayama's lemma gives $M = \mathrm{Lie}(G^\vee)$. Choose $F_j$ for $l_j$.
2. *Logarithms exist.* We take as given that for a formal group law over $O$ and a vector $a \in O^d$, there is a series $\ell$ over $E$ with constant term $0$, with linear part $a$ and with $\delta^1 \ell = 0$. Take $\ell_i$ for the $i$-th unit vector. Put $e_{(1,i)} = \ell_i$ and $e_{(2,j)} = F_j$. Each member is a quasi-logarithm relative to $O$, and parts 2, 3 and 4 hold by construction.
3. *Uniqueness.* For each $i$ the series $\ell_i$ is a quasi-logarithm, and we take as given that each quasi-logarithm is a Lie series for some $l$. Since the defects of $\ell_i$ vanish, that $l$ is $0$. Let $b$ be a vector with $\sum b_i e_i$ integral. The combination is a Lie series for $\sum_j b_{(2,j)} l_j$, and an integral Lie series belongs to $l = 0$. So $\sum_j b_{(2,j)} l_j = 0$, and all $b_{(2,j)}$ vanish because the $l_j$ are a basis. Then $s = \sum_i b_{(1,i)} \ell_i$ is integral and $\delta^1 s = 0$. We take as given that an integral series $s$ over $O$ with $\delta^1 s = 0$ for the law of a chart is zero. So $s = 0$, and the coefficient of $X_i$ gives $b_{(1,i)} = 0$, since $O \to E$ is injective.
4. *Existence.* We take as given that $f - \sum b_i e_i$ can be made integral for each quasi-logarithm $f$ relative to $O$. This follows from a division step: modulo integral series and $p$ times quasi-logarithms, each quasi-logarithm is a combination of the $e_i$, and $p$-adic completeness of $O$ lets one iterate. If $b$ and $b'$ both work, then $\sum (b'_i - b_i) e_i$ is integral, and step 3 gives $b = b'$. So part 1 holds. $\square$

The theorem gives $d + k$ quasi-logarithms. The next sections show that $d + k$ is the height of $G$, after the basis is lifted to a frame over $A_{\inf}$.

**Remark 5.1.7 (Formalization).** The theorem is in [ExistsAdaptedQuasiLogBasisPDivGroupLieDual.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsAdaptedQuasiLogBasisPDivGroupLieDual.lean#L175), and the Nakayama step is `exists_isLie` at line 144 of the same file. Frames, quasi-logarithms, bases, adapted families and Lie series are `IsFrame`, `QL`, `IsBasis`, `IsAdapted` and `Chart.IsLie` in [EqZeroOfForallPowDvd.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EqZeroOfForallPowDvd.lean#L19). The facts we take as given are the `GlobalTheory.T` statements `omega_finite_projective`, `exists_quasiLogarithm_lie_add_p_smul`, `exists_formalGroupLaw_log_with_linearPart`, `pDivGroup_dual_tangent_of_quasiLogarithm`, `pDivGroupChart_integral_additive_series_eq_zero`, `quasiLogarithm_generation_of_division_step_padic` and `quasiLogarithm_division_step_decomposition`; we read their statements and did not open their proofs, so the reasons we give for step 4 are the usual ones. The theorem holds for any frame $(O, E, \mathrm{id})$, but the only use, in HasPeriodIntegral.lean, takes $E = C$. The wrapper proves its statement by `first | exact @X | exact X | ...`, as all wrappers of this chapter do.

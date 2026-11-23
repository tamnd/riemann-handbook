---
title: The Jacquet-Shalika bound
decls:
  - PositivityTheory.JacquetShalikaLocal.jacquetShalikaBound
  - PositivityTheory.JacquetShalikaLocal.l10
  - PositivityTheory.JacquetShalikaLocal.l6
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Jacquet-Shalika bound

This section proves the bound of Jacquet and Shalika for the Satake parameters of a cuspidal automorphic representation of $\mathrm{GL}_a$ with unitary central character: at each unramified finite place $w$, every parameter $\alpha$ satisfies $N(w)^{-1/2} < |\alpha| < N(w)^{1/2}$. The bound is used in the step [EveryCharacter](/step/every-character/), and it is an input of the pole of the Rankin-Selberg $L$-function in the next section ([Theorem 9.14.5](/entry/rs-pole/)). The proof is local. A positive form on the local representation, built by averaging the invariant inner product over the columns of the mirabolic subgroup, bounds a weighted sum of squares of the spherical Whittaker function along a torus. The formula of Shintani turns this into a statement on a generating function, whose poles are the inverse parameters. See [automorphic representations](/learn/automorphic-forms/#automorphic-representations), [Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions) and [unramified representations](/learn/representations/#unramified-representations).

**Definition 9.13.1 (Cuspidal representations and Satake parameters).** Let $E$ be a number field and $a \geq 0$. A *cuspidal representation* of $\mathrm{GL}_a$ over $E$ is a nonzero space $V$ of smooth cusp forms on $\mathrm{GL}_a(E) \backslash \mathrm{GL}_a(\mathbb{A}_E)$ that is stable under right translation by $\mathrm{GL}_a(\mathbb{A}_{E,f})$, under the maximal compact subgroup at infinity and under the Lie algebra at infinity, and that has no stable subspace other than $0$ and $V$. Two of them are equivalent if there is a linear isomorphism that commutes with all these operators. For a finite place $w$ of $E$, let $E_w$ be the completion, $\mathcal{O}_w$ its ring of integers, $q_w = N(w)$ the order of the residue field and $K_w = \mathrm{GL}_a(\mathcal{O}_w)$. Let $\pi_w$ be the action of $\mathrm{GL}_a(E_w)$ on $V$. A multiset $B$ of $a$ nonzero complex numbers is the *Satake multiset* of $V$ at $w$ if $V^{K_w} \neq 0$ and each nonzero $v \in V^{K_w}$ satisfies, for each uniformizer $\varpi$ and each $0 \leq j \leq a$,
$$T_j v = q_w^{j(a-j)/2} \, e_j(B) \, v,$$
where $T_j$ is the Hecke operator of the double coset $K_w \operatorname{diag}(\varpi, \ldots, \varpi, 1, \ldots, 1) K_w$ (with $j$ entries $\varpi$) and $e_j$ is the $j$-th elementary symmetric function. The representation has *unitary central character* if the centre $\mathbb{A}_E^\times$ acts on $V$ by a Hecke character of absolute value $1$.

**Theorem 9.13.2 (Jacquet-Shalika bound).** Let $E$ be a totally complex number field and $V$ a cuspidal representation of $\mathrm{GL}_a$ over $E$ with unitary central character. Let $w$ be a finite place and $B$ the Satake multiset of $V$ at $w$. Then each $\alpha \in B$ satisfies
$$N(w)^{-1/2} < |\alpha| < N(w)^{1/2}.$$

Lean: `PositivityTheory.JacquetShalikaLocal.jacquetShalikaBound`.

We prove the theorem at the end of the section. First we work over a local field.

**Definition 9.13.3 (Local setting).** Let $F$ be a nonarchimedean local field with ring of integers $\mathcal{O}$, uniformizer $\varpi$ and residue field of order $q$, and let $s = q^{1/2}$. Fix a Haar measure on $F$ and a character $\psi : F \to \mathbb{C}^\times$ of absolute value $1$ that is trivial on $\mathcal{O}$ and not trivial on $\varpi^{-1}\mathcal{O}$. Let $N \subseteq \mathrm{GL}_n(F)$ be the upper unipotent subgroup, with the character $\psi_N(u) = \psi(u_{12} + u_{23} + \cdots + u_{n-1,n})$. Let $\rho$ be a smooth representation of $\mathrm{GL}_n(F)$ on a complex vector space $V$: each vector is fixed by a congruence subgroup $1 + \varpi^{c}\mathrm{M}_n(\mathcal{O})$.

1. A *Whittaker functional* is a linear form $\lambda$ on $V$ with $\lambda(\rho(u)x) = \psi_N(u)\lambda(x)$ for $u \in N$.
2. An *invariant inner product* is a sesquilinear form $\langle\, , \rangle$ on $V$ that is hermitian, positive definite, and invariant under $\rho$.
3. A vector $v$ is *spherical with parameters* $z = (z_1, \ldots, z_n) \in (\mathbb{C}^\times)^n$ if it is fixed by $\mathrm{GL}_n(\mathcal{O})$ and $T_j v = s^{j(n-j)} e_j(z) v$ for $0 \leq j \leq n$.

Let $a_j = \operatorname{diag}(\varpi^j, 1, \ldots, 1)$. The key local estimate is the following.

**Proposition 9.13.4 (A positive form with a Bessel bound).** Let $n > 1$, let $\lambda$ be a Whittaker functional on $V$ and $\langle\, , \rangle$ an invariant inner product. Then there is a sesquilinear form $\beta$ on $V$ with these properties.

1. $\beta$ is hermitian and $\operatorname{Re}\beta(x, x) \geq 0$ for all $x$.
2. If $\beta(x, x) = 0$, then $\lambda(x) = 0$.
3. For each $y$, the form $x \mapsto \beta(y, x)$ is a Whittaker functional.
4. For each $\mathrm{GL}_n(\mathcal{O})$-fixed vector $v$ there is a constant $C$ with
$$\sum_{j=0}^{T-1} q^{j(n-2)} \operatorname{Re}\beta(\rho(a_j)v, \rho(a_j)v) \leq C \quad \text{for all } T.$$

Lean: `PositivityTheory.JacquetShalikaLocal.l6`.

*Proof.* For $0 \leq k \leq n-1$ let $P_k$ be the group of $g \in \mathrm{GL}_n(F)$ whose rows of index $> k$ and whose columns of index $> k + 1$ are those of the identity (indices from $1$), and let $N_k$ be the group of $u \in N$ whose first $k+1$ columns are those of the identity. Say that a form $\beta_k$ is *good at level $k$* if it is hermitian with $\operatorname{Re}\beta_k(x,x) \geq 0$, if $\beta_k(x,x) = 0$ implies $\lambda(x) = 0$, if $\beta_k(\rho(g)x, \rho(g)y) = |\det g|^{n-1-k}\beta_k(x,y)$ for $g \in P_k$, and if $\beta_k(y, \rho(u)x) = \psi_N(u)\beta_k(y,x)$ for $u \in N_k$. The invariant inner product is good at level $n-1$: there $P_{n-1}$ is the mirabolic subgroup, the exponent is $0$, and $N_{n-1}$ is trivial.

Let $X_k$ be the group of matrices $1 + x$, where $x$ has its only nonzero entries in the first $k+1$ rows of column $k+2$. If $\beta_{k+1}$ is good at level $k+1$, put
$$\beta_k(y, x) = \lim_{M \to \infty} \int_{\varpi^{-M}\mathcal{O}^{k+1}} \psi(-x_{k+1}) \, \beta_{k+1}(y, \rho(1 + x)x) \, dx.$$
The integral is constant for large $M$ by smoothness, so the limit exists. Then $\beta_k$ is good at level $k$. Hermitian symmetry and positivity come from writing $\beta_k(x,x)$ as the limit of the $\beta_{k+1}$-norm of an average of translates of $x$. The quasi-invariance comes from the change of variables $x \mapsto t x$ for the action of $P_k$ on $X_k$ by conjugation, which multiplies the measure by $|\det g|$. The equivariance under $N_k$ comes from the decomposition $N_k = N_{k+1} X_k$ and the factor $\psi(-x_{k+1})$.

Starting from $\langle\, , \rangle$ and descending from level $n-1$ to level $0$ gives $\beta = \beta_0$, which has properties 1 to 3, since $N_0 = N$. Property 4 is the estimate for the last averaging step, from level $1$ to level $0$: it bounds the sum by the $\beta_1$-norm of an average of translates of $v$ over a compact set, with the factor $q^{j(n-2)} = |\det a_j|^{-(n-2)}$ from the quasi-invariance at level $1$. $\square$

**Lemma 9.13.5 (Shintani's formula).** (T. Shintani, Proc. Japan Acad. 52 (1976).) Let $v$ be spherical with parameters $z$ and $\lambda$ a Whittaker functional. Then $\lambda(\rho(g)v) = \lambda(v) W_z(g)$ for all $g$, where $W_z$ is the normalised spherical Whittaker function. In particular
$$\lambda(\rho(a_j)v) = \lambda(v) \, s^{-(n-1)j} \, h_j(z),$$
where $h_j$ is the complete homogeneous symmetric function of degree $j$. The functions $h_j$ satisfy $h_0 = 1$ and, for $j \geq 1$,
$$\sum_{r=0}^{j} (-1)^r e_r(z) \, h_{j-r}(z) = 0.$$

Lean: `PositivityTheory.JacquetShalikaLocal.l7` (also `PositivityTheory.JacquetShalikaLocal.l8`, the recursion, and `PositivityTheory.JacquetShalikaLocal.l9`, the fact on the recursion below).

*Proof.* We take the formula as given, from Shintani's paper. The recursion is the identity $\sum_j h_j t^j = \prod_i (1 - z_i t)^{-1}$. $\square$

The recursion gives the following elementary fact: if $\beta \in \mathbb{C}^n$ and a sequence $g_j$ satisfies $g_0 = 1$, the recursion $\sum_{r=0}^{j}(-1)^r e_r(\beta) g_{j-r} = 0$ for $j \geq 1$, and $g_j \to 0$, then $|\beta_i| < 1$ for all $i$. Indeed, then $\sum_j g_j t^j = \prod_i (1 - \beta_i t)^{-1}$, and a power series with bounded coefficients converges for $|t| < 1$, while the product has a pole at $t = \beta_i^{-1}$; a pole on the circle $|t| = 1$ is excluded because the coefficients tend to $0$.

**Proposition 9.13.6 (Upper bound for the parameters).** Let $n > 1$, let $\lambda$ be a Whittaker functional and $\langle\, , \rangle$ an invariant inner product on $V$. Let $v$ be spherical with parameters $z$, and assume that $\lambda(\rho(g)v) \neq 0$ for some $g$. Then $|z_i| < q^{1/2}$ for all $i$.

Lean: `PositivityTheory.JacquetShalikaLocal.l10`.

*Proof.* By Shintani's formula, $\lambda(v) \neq 0$. Let $\beta$ be the form of the Proposition above, and put $c = \beta(v, v)$. Then $c \neq 0$ by property 2. By property 3, $x \mapsto \beta(v, x)$ is a Whittaker functional, so Shintani's formula gives $\beta(v, \rho(a_j)v) = c \, s^{-(n-1)j} h_j(z)$. Put $g_j = h_j(z) / s^j$. The Cauchy-Schwarz inequality for the positive semidefinite form $\beta$ gives
$$|c|^2 s^{-2(n-1)j} |h_j(z)|^2 \leq \operatorname{Re}(c) \operatorname{Re}\beta(\rho(a_j)v, \rho(a_j)v).$$
Since $s^{2(n-1)j} s^{-2j} = q^{j(n-2)}$, this is $|c|^2|g_j|^2 \leq \operatorname{Re}(c) \, q^{j(n-2)} \operatorname{Re}\beta(\rho(a_j)v, \rho(a_j)v)$. Property 4 now gives $\sum_j |g_j|^2 \leq \operatorname{Re}(c) C / |c|^2$, so $g_j \to 0$. The sequence $g_j = h_j(z/s)$ satisfies $g_0 = 1$ and the recursion with $\beta = z/s$. By the fact after Shintani's formula, $|z_i/s| < 1$. $\square$

*Proof of the theorem.* Let $w$ be a finite place with Satake multiset $B$, let $\alpha \in B$, and let $n = a$, so $n \geq 1$. Write $B = \{z_1, \ldots, z_n\}$ and let $F = E_w$, $q = N(w)$. We use four facts about the local component $\pi_w$ on $V$, which are proved separately and which we take as given here. (i) It is smooth. (ii) It has a nonzero Whittaker functional $\lambda$ for some $\psi$ as above; this comes from the Fourier expansion of cusp forms ([Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions)). (iii) It has an invariant inner product; this is the Petersson inner product, which is defined because the central character is unitary. (iv) For each nonzero linear form $\lambda$ on $V$ there are a nonzero $\mathrm{GL}_n(\mathcal{O}_w)$-fixed vector $v$ and an element $g \in \mathrm{GL}_n(E_w)$ with $\lambda(\pi_w(g)v) \neq 0$. Each nonzero fixed vector is spherical with parameters $z$, by the definition of the Satake multiset.

Upper bound. If $n > 1$, the Proposition gives $|z_i| < q^{1/2}$. 

Unitarity. The invariant inner product and the Hecke relations give $\overline{e_r(z)} \, e_n(z) = e_{n-r}(z)$ for $0 \leq r \leq n$: the adjoint of $T_r$ for the inner product is $T_{n-r}$ composed with the action of the central element $\varpi^{-1} \cdot 1$, and $\varpi \cdot 1$ acts on $v$ by $e_n(z)$. These relations say that the multisets $\{\bar z_i^{-1}\}$ and $\{z_i\}$ have the same elementary symmetric functions, so for each $i$ there is $j$ with $|z_j| |z_i| = 1$. If $n = 1$, then $j = i$ and $|z_i| = 1 < q^{1/2}$. So $|z_i| < q^{1/2}$ for all $i$ in all cases.

Lower bound. For $\alpha = z_i$, choose $j$ with $|z_j||z_i| = 1$. Then $|\alpha| = |z_j|^{-1} > q^{-1/2}$. $\square$

For the classical theorem with $n = 2$ and a cusp form of weight $k$ on $\mathrm{GL}_2(\mathbb{Q})$, normalised so that the central character is unitary, the bound says $|\alpha_p| < p^{1/2}$, a weak form of the Ramanujan bound $|\alpha_p| = 1$. The point of the theorem is that it holds for all $n$ with no arithmetic input.

**Remark 9.13.7 (Formalization).** The statement is `JacquetShalikaBound` at [StrongMultiplicityOne.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/StrongMultiplicityOne.lean#L197). It asks that $E$ be totally complex, which the classical theorem does not need, and `IsUnitary` (L89) only asks for a unitary central character. Every theorem in [JacquetShalikaBound.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaBound/JacquetShalikaBound.lean#L1) is a theorem of `GlobalTheory.CompanionTheory` with its type written out; `jacquetShalikaBound` is `jacquetShalikaBound_of_steps` applied to `l10`, `l11`, `l11b`, `l12` and `g1` to `g4`, and `l6` is `final_form_bessel_bound` applied to `l4a` to `l4d` and `l5`, which are the averaging steps of the proof above (`StableAverageExists`, `FormHermitianPositive`, `FormQuasiInvariantMirabolic`, `FormEquivariantColumn`) and the last estimate `L5`. We read the statements of these steps, not their proofs; the order of the descent in the proof above is our reading of these statements. The proof of `l10` is `Satake.l10` in [TendstoZeroOfSumSqLe.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TendstoZeroOfSumSqLe.lean#L105), and it follows the proof above line by line. Shintani's formula is the input `L7` together with `sphericalWhittaker_torusPow`, which we did not open. Three names do not describe their statements: `lift_levelP_alt₂` says that a Satake vector is spherical with the same parameters, `liftZP_unit` is the unitarity relation $\overline{e_r} e_n = e_{n-r}$, and `liftZP_newton` is the fact on the recursion. Structures named `CuspSub` are defined in three files (namespaces `GlobalTheory.CuspRep`, `GlobalTheory.CuspNF` and one in `RealCusp.lean`); the theorem uses the one in `GlobalTheory.CuspRep`.

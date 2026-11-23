---
title: Hilbert modular forms congruent to one
decls:
  - GlobalTheory.HilbertThetaSeries.seed_exists
  - GlobalTheory.T.exists_seed_theta_lattice_fixedPointFree
  - GlobalTheory.HilbertThetaSeries.hilbertOne
  - UpperTheory.V.Published.exists_hilbertModularForm_congr_one
  - UpperTheory.V.Lit.oneUse
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hilbert modular forms congruent to one

This section proves that over each totally real field $F$ and for each odd prime $p$ there are holomorphic Hilbert modular forms of level one whose $q$-expansions are $p$-adically close to $1$, in all weights divisible by $(p-1)p^N$ for some $N$. For $F = \mathbb{Q}$ the Eisenstein series $E_{p-1}$ has this property [Serre 1973]. For a general $F$ we build the form from the theta series of an even lattice of rank $2(p-1)$ with a fixed point free isometry of order $p$. The result fills the input "a form congruent to 1 in a large weight" of [the case II seed](/entry/seed-iis-alt/). The background is in [theta series of lattices](/learn/theta-functions-cm/#theta-series-of-lattices), [modular forms](/learn/automorphic-forms/#modular-forms), [automorphic forms on adelic groups](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups) and [places and completions](/learn/number-fields/#places-and-completions).

### The theta seed

Let $F$ be a totally real field of degree $d$ with real places $v$, and let $\mathbb{H}^F$ be the product of $d$ copies of the upper half plane. Fix a prime $p$ and an isomorphism $\iota \colon \overline{\mathbb{Q}}_p \to \mathbb{C}$. For $\xi \in F$ put $e(\xi z) = \exp(2\pi i \sum_v v(\xi) z_v)$. For $h \in \mathrm{GL}_2(\mathbb{R})^d$ let $f|_k h$ be the slash operator of weight $k$ with the automorphy factor $\prod_v (c_v z_v + d_v)^{-k}$ and no determinant factor.

**Definition 5.7.1.** Let $f \colon \mathbb{H}^F \to \mathbb{C}$.

1. $f$ is *holomorphic* if it is complex differentiable on $\mathbb{H}^F$, and of *moderate growth* if $|f(z)| \leq C \prod_v \bigl((1 + |z_v|^2)/\mathrm{Im}\, z_v\bigr)^A$ for some $C$ and $A$.
2. $f$ has a *$q$-expansion* $a \colon F \to \mathbb{C}$ if there is $D > 0$ such that each $\xi$ with $a(\xi) \neq 0$ is $0$ or totally positive with $D\xi$ integral, and $f(z) = \sum_\xi a(\xi)\, e(\xi z)$ for each $z$.
3. $f$ is *$r$-small* if it has a $q$-expansion $a$ with $|\iota^{-1}(a(\xi))| \leq r$ for each $\xi$.

**Definition 5.7.2.** An element $\delta \in F$ is a *local generator of the inverse different at $p$* if $\mathrm{ord}_w \delta = -\mathrm{ord}_w \mathfrak{d}_F$ for each prime $w \mid p$. For such $\delta$, a matrix $\gamma \in \mathrm{GL}_2(F)$ is *$p$-integral for $\delta$* if $\gamma_{11}$, $\delta\gamma_{12}$, $\gamma_{21}/\delta$ and $\gamma_{22}$ are integral at each $w \mid p$, $\det \gamma$ is a unit at each $w \mid p$, and $\det\gamma$ is totally positive.

**Definition 5.7.3.** A *seed* for $\iota$ and $\delta$ is a function $\theta \colon \mathbb{H}^F \to \mathbb{C}$ with:

1. $\theta$ is holomorphic and of moderate growth;
2. for each $\gamma$ that is $p$-integral for $\delta$, the function $\theta|_{p-1}\gamma - 1$ is $1/p$-small;
3. there is $N > 0$ such that for each $\gamma \in \mathrm{SL}_2(\mathcal{O}_F)$ with $\gamma_{21} \in N\mathcal{O}_F$, $\theta|_{p-1}\gamma = \zeta\theta$ for some $\zeta$ with $\zeta^8 = 1$.

**Theorem 5.7.4 (a theta seed exists).** Let $F$ be totally real, $p$ an odd prime, $\iota \colon \overline{\mathbb{Q}}_p \to \mathbb{C}$ an isomorphism and $\delta$ a local generator of the inverse different at $p$. Then there is a seed for $\iota$ and $\delta$.

Lean: `GlobalTheory.HilbertThetaSeries.seed_exists` (also `GlobalTheory.T.exists_seed_theta_lattice_fixedPointFree`, a second name)

*Proof.* The proof has these steps.

1. There are an index set $\kappa$ of size $2(p-1)$, a matrix $G \in M_\kappa(\mathbb{Z})$, a matrix $S \in M_\kappa(\mathbb{Z})$ and $t \in \mathbb{N}$ with these properties: $G$ is positive definite with even diagonal; $S^T G S = G$; $1 + S + \cdots + S^{p-1} = 0$; $\det G = t^2$; and $(-1)^{(p-1)/2}\, t \equiv 1 \pmod p$. The relation $1 + S + \cdots + S^{p-1} = 0$ says that $S$ is an isometry of order $p$ with no nonzero fixed vector.
2. Put $Q(x) = \tfrac{1}{2} x^T G x$ and
$$\theta(z) = \sum_{x \in \mathcal{O}_F^\kappa} e\bigl(Q(x) z\bigr).$$
The coefficients are $1$ on the lattice $\mathcal{O}_F^\kappa$ and $0$ off it, so they are bounded. A theta series with bounded coefficients supported on a lattice is holomorphic and of moderate growth.
3. Since $\det G$ is a square and $|\kappa| = 2(p-1)$, there is $N > 0$ such that $\theta$ is modular of weight $p - 1$ for the matrices of determinant 1 in level $N$, up to an eighth root of unity.
4. For $\gamma$ that is $p$-integral for $\delta$, a lemma on the translates of this theta series shows that $\theta|_{p-1}\gamma - 1$ is $1/p$-small. Its inputs are the isometry $S$, which has no nonzero fixed vector, and the congruence on $t$. $\square$

### Forms of level one congruent to one

Let $\mathbb{A}_f$ be the finite adeles of $F$ and $K = \mathrm{GL}_2(\widehat{\mathcal{O}}_F)$. A *holomorphic form of parallel weight $k$ and level one* is a function $\varphi$ on $\mathrm{GL}_2(\mathbb{A}_F)$ that is left invariant under $\mathrm{GL}_2(F)$, right invariant under $K$, with trivial central character, and whose restriction to each component is a holomorphic function of moderate growth of weight $k$. It has an *adelic $q$-expansion* with constant terms $c_0(y)$ for $y \in \mathbb{A}_f^\times$ and coefficients $c(\mathfrak{m})$ for integral ideals $\mathfrak{m}$. We do not unfold the two predicates.

**Theorem 5.7.5 (forms congruent to one).** Let $F$ be totally real, $p$ an odd prime and $\iota \colon \overline{\mathbb{Q}}_p \to \mathbb{C}$ an isomorphism. There is $N$ such that for each $k > 0$ with $(p-1)p^N \mid k$ there is a holomorphic form $\varphi$ of parallel weight $k$ and level one with trivial central character, with adelic $q$-expansion $(c_0, c)$, such that
$$|\iota^{-1}(c_0(y)) - 1| < 1 \text{ for each } y, \qquad |\iota^{-1}(c(\mathfrak{m}))| < 1 \text{ for each } \mathfrak{m} \neq 0.$$

Lean: `GlobalTheory.HilbertThetaSeries.hilbertOne` (also `UpperTheory.V.Published.exists_hilbertModularForm_congr_one`, a second name)

*Proof.* The proof has these steps.

1. Choose a totally positive local generator $\delta$ of the inverse different at $p$, and a seed $\theta$ for $\iota$ and $\delta$.
2. A finite set $Y$ of finite ideles gives the decomposition
$$\mathrm{GL}_2(\mathbb{A}_f) = \bigcup_{y \in Y} \mathrm{GL}_2(F)^+ \begin{pmatrix} y & 0 \\ 0 & 1 \end{pmatrix} K.$$
Each $y \in Y$ is adapted to $\delta$ at the primes above $p$.
3. For each $y \in Y$, an average of powers of $\theta$ over the orbit of the stabilizer of the coset of $y$ gives $N_y$ with this property: for each $M$ with $p^{N_y} \mid M$ there is a holomorphic function $f_y$ of moderate growth and weight $(p-1)M$, invariant under that stabilizer, with $f_y|\gamma - 1$ $1/p$-small for each $\gamma$ that is $p$-integral for $\delta$.
4. Let $N = \max_y N_y$ and $k = (p-1)p^N m$. The functions $|y|^{k/2} f_y$ glue to a system $\Psi$ on $\mathrm{GL}_2(\mathbb{A}_f)$ that is left invariant under $\mathrm{GL}_2(F)^+$ through the slash action, right invariant under $K$ and invariant under the center.
5. Since $p$ is odd, $k$ is even. So $\Psi$ lifts to a holomorphic adelic form $\varphi$ of weight $k$ and level one with trivial central character.
6. For each $y$, the component $|y|^{-k/2}\Psi(y) - 1$ is $1/p$-small. A $q$-expansion $a_y$ of $|y|^{-k/2}\Psi(y)$ thus has $|\iota^{-1}(a_y(0)) - 1| < 1$ and $|\iota^{-1}(a_y(1))| < 1$, since $1/p < 1$.
7. The adelic $q$-expansion of the lift has $c_0(y) = a_y(0)$, and for each $\mathfrak{m} \neq 0$ there is $y$ with $c(\mathfrak{m}) = a_y(1)$. $\square$

The hypothesis $k > 0$ is not used in the proof: the weight is $(p-1)p^N m$ for any $m$.

**Theorem 5.7.6 (a form congruent to one in a large weight).** Let $F$ be totally real, $p$ an odd prime, $\iota \colon \overline{\mathbb{Q}}_p \to \mathbb{C}$ an isomorphism and $B \in \mathbb{N}$. There are $k \geq B$ with $k > 0$ and $p - 1 \mid k$, and a holomorphic form $\varphi$ of parallel weight $k$ and level one with trivial central character, with adelic $q$-expansion $(c_0, c)$, such that $|\iota^{-1}(c_0(y)) - 1| < 1$ for each $y$ and $|\iota^{-1}(c(\mathfrak{m}))| < 1$ for each $\mathfrak{m} \neq 0$.

Lean: `UpperTheory.V.Lit.oneUse`

*Proof.* Take $N$ from the previous theorem and put $k = (p-1)p^N(B+1)$. Then $k > 0$, $k \geq B + 1 > B$, $p - 1 \mid k$ and $(p-1)p^N \mid k$. The previous theorem gives $\varphi$. $\square$

**Remark 5.7.7 (Formalization).** The seed theorem is in [ExistsSeedThetaLatticeFixedPointFree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ExistsSeedThetaLatticeFixedPointFree.lean#L12). Its second name at lines 33 to 35 restates the same type and proves it with a `first | exact ... | ...` combinator under `set_option maxHeartbeats 1000000`; one `exact` would do. The name says "fixedPointFree", but the statement only asks for a seed; the fixed point free isometry appears only inside the proof. The steps of the proof are `GlobalTheory.T.exists_evenPositiveDefinite_intMatrix_det_sq`, `GlobalTheory.T.thetaSeries_holomorphic_qExpansion_of_bounded_coeff`, `GlobalTheory.T.theta_slash_eighth_root_of_square_det` and `GlobalTheory.T.theta_translate_integral_congruent_one_mod_prime`; we have not unfolded their proofs. The seed is `Seed` and the lattice data are `LatD` ([EvenPos.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/EvenPos.lean#L84)). The second theorem is in [HasQOfSmallSubOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/HasQOfSmallSubOne.lean#L33). It calls the seed theorem by its second name. The hypothesis $0 < k$ is dropped at [line 47](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/HasQOfSmallSubOne.lean#L47). The proof gives each coefficient within $1/p$, but the statement keeps only the bound $< 1$. Its statement is `HilbertOne` ([Hilbert.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/Hilbert.lean#L18)), with `IsHol k (fun _ => 0) 1 φ` and `HasExp`, which we do not unfold. The second name is at [ExistsHilbertModularFormCongrOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ExistsHilbertModularFormCongrOne.lean#L6). It lives in the namespace `Published`, but the result is proved in this development and is not a cited theorem. The last theorem is at [line 8](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ExistsHilbertModularFormCongrOne.lean#L8) of the same file; it applies `oneUse_of` from [OneUseOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/OneUseOf.lean#L9). The statement `OneUse` fills the field `one` of `Hypotheses4Z'` ([Hypotheses4Z.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/Hypotheses4Z.lean#L9)).

## Notes and references

This chapter feeds two parts of the [window bound](/proof/vwin/). Sections 1 to 5 give [the unramified zeta theorem](/entry/zeta-ur/): the coefficient law of smoothed zeta classes, Kato's norm-compatible system with its integrality, and the nonvanishing on inertia by Coleman power series. Section 6 gives the core statement on ordinary adjoint cocycles that [the core argument](/entry/core-o-of-literal-automorphy-n/) uses. Section 7 gives the form congruent to one that [the case II seed](/entry/seed-iis-alt/) needs.

- R. F. Coleman, Division values in local fields, Invent. Math. 53 (1979), 91 to 116.
- H. Hida, Elementary Theory of L-functions and Eisenstein Series, London Math. Soc. Student Texts 26, Cambridge University Press, 1993, Chapter 7.
- K. Kato, P-adic Hodge theory and values of zeta functions of modular forms, Astérisque 295 (2004), 117 to 290.
- K. Rubin, Euler Systems, Annals of Mathematics Studies 147, Princeton University Press, 2000.
- J.-P. Serre, A Course in Arithmetic, Graduate Texts in Mathematics 7, Springer, 1973, Chapter VII.
- J.-P. Serre, Formes modulaires et fonctions zêta p-adiques, in Modular Functions of One Variable III, Lecture Notes in Math. 350, Springer, 1973, 191 to 268.
- L. C. Washington, Introduction to Cyclotomic Fields, 2nd ed., Graduate Texts in Mathematics 83, Springer, 1997, Chapter 13.

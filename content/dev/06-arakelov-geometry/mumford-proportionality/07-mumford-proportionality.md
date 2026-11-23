---
title: Mumford proportionality
decls:
  - GlobalTheory.LieBase.exists_goodBase
  - GlobalTheory.Proportionality.mumfordProportionality_of_goodChernWeil
  - GlobalTheory.T.toroidalFlagProportionality_of_goodChernWeil
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mumford proportionality

This section proves the main theorem of the chapter: on a toroidal flag space of a unitary Shimura variety, the top self-intersection of the automorphic line bundle $L_\lambda$ is the covolume of the arithmetic group times the flag degree of $\lambda$. This is the Hirzebruch-Mumford proportionality theorem in the form of D. Mumford, "Hirzebruch's proportionality theorem in the non-compact case", Invent. Math. 42 (1977), 239 to 272. The proof takes one input as a hypothesis: Mumford's theorem that Chern forms of good metrics compute Chern numbers, together with the push-forward formula for full flag bundles. The analytic part, which is the subject of the previous sections, is collected in one theorem, [the good base](/entry/exists-good-base/).

We keep the notation of the previous sections: the moduli space $Z$ with its toroidal model, a complex embedding $\sigma$ with the condition `GoodEmb`, the uniformization $U$ with components $U_k$, and a toroidal flag space $\Phi$ with components $Y_k$ ([toroidal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications)).

**Definition 7.7.1 (Graded flag refinement).** Let $X$ and $Y$ be varieties over $F$, and let $\mathcal{E}$ be a framed family of bundles of ranks $(m_\tau)_{\tau \in I}$ on $X$. A *flag refinement* of $\mathcal{E}$ on $Y$ is a morphism $f \colon Y \to X$, with the map $\varphi$ of function fields, and a framed family $\mathcal{E}'$ on $Y$ whose frames differ from the pulled back frames of $\mathcal{E}$ by matrices of triangular form over the local rings, such that for each field $K$, each $K$-point $x$ of $X$ and each full flag of the fibre of $\mathcal{E}$ at $x$ there is exactly one $K$-point of $Y$ over $x$ that carries this flag. So $Y$ is the full flag bundle of $\mathcal{E}$. The refinement is *graded* by divisors $D_{\tau,i}$ on $Y$, for the roots $(\tau, i)$, if the diagonal entries of the transition matrices of $\mathcal{E}'$ are local equations of the $D_{\tau,i}$. Then $\mathcal{O}(D_{\tau,i})$ is the $i$-th graded line bundle of the universal flag of $\mathcal{E}_\tau$.

**Definition 7.7.2 (Intersection polynomial).** Let $Y$ be a variety of dimension $d$ with divisors $D_x$ indexed by a finite set. The *intersection polynomial* is the linear map $I_D \colon \mathbb{R}[x] \to \mathbb{R}$ with
$$I_D\Bigl(\prod_{i=1}^{d} x_{s(i)}\Bigr) = \bigl(D_{s(1)} \cdots D_{s(d)}\bigr)_Y$$
for every map $s \colon \{1, \dots, d\} \to$ (indices), and $I_D(\text{monomial}) = 0$ for monomials of degree other than $d$. The value does not depend on the order of the factors, because the intersection number is symmetric. So $I_D(P)$ is the degree of the class $P(D)$ in top degree.

The intersection number $(D_1 \cdots D_d)_Y$ is defined from the Euler characteristic: it is the mixed difference of $(a_1, \dots, a_d) \mapsto \chi(\mathcal{O}(\sum_i a_i D_i))$ at $0$, as in the theory of Snapper and Kleiman ([coherent cohomology](/learn/commutative-algebra/#coherent-cohomology)). Section 12 works with a form of this definition, with $h^0$ of large twists in place of $\chi$.

**Definition 7.7.3 (Fibre point).** With the roots $x_{\tau,i}$, $0 \leq i < m_\tau$, put
$$\varphi = \prod_{(\tau, i)} (-x_{\tau,i})^{m_\tau - 1 - i}.$$
This is the class of a point in the fibre of the full flag bundle.

**Definition 7.7.4 (Good Chern-Weil theory).** *Good Chern-Weil theory* is the conjunction of the two statements below. In both, $f \colon Y \to X$ is a flag refinement of $\mathcal{E}$, graded by divisors $D$.

1. *Good Chern numbers.* For every open $O \subseteq X$, every Hermitian metric $h$ on $\mathcal{E}$ over $O$ that is good, and every $R \in \mathbb{R}[c_{\tau,k}]$,
$$\int_O R(c(h)) = I_D\bigl(\chi(R)\,\varphi\bigr).$$
2. *Push-forward from the flag bundle.* If $F$ has characteristic $0$, then for all $Q \in \mathbb{R}[x_{\tau,i}]$ and $R \in \mathbb{R}[c_{\tau,k}]$ with $\operatorname{antisym}(Q) = \chi(R)\,\Delta$,
$$I_D(Q) = I_D\bigl(\chi(R)\,\varphi\bigr).$$

The [good metrics](/entry/lie-gram-is-good/), the [Chern integral](/entry/has-chern-integral-point-poly-covol/), $\chi$, $\Delta$ and $\operatorname{antisym}$ are as in the previous sections. The first statement is Mumford's theorem on good metrics, read on the flag bundle: $\chi(R)\,\varphi$ pushes forward to $R(c(\mathcal{E}))$ on $X$. The second statement says that the push-forward of $Q$ to $X$ is $R(c(\mathcal{E}))$ when $\operatorname{antisym}(Q) = \chi(R)\Delta$. Both are theorems in the literature. Here we take them as a hypothesis. They are proved as [good Chern-Weil theory](/entry/good-chern-weil/) in another chapter.

**Proposition 7.7.5 (Chern integrals as flag intersections).** Assume good Chern-Weil theory. Let $f \colon Y \to X$ be a flag refinement of $\mathcal{E}$ graded by $D$, and let $h$ be a good metric on $\mathcal{E}$ over $O$, with $\sigma$ an embedding of $F$ in $\mathbb{C}$. If $\operatorname{antisym}(Q) = \chi(R)\,\Delta$, then $\int_O R(c(h)) = I_D(Q)$.

*Proof.* Since $F$ embeds in $\mathbb{C}$, it has characteristic $0$. The push-forward statement gives $I_D(Q) = I_D(\chi(R)\,\varphi)$, and the statement on good Chern numbers gives $\int_O R(c(h)) = I_D(\chi(R)\,\varphi)$. $\square$

**Theorem 7.7.6 (The good base).** Let $k$ be a component. There are a variety $X$, a framed family $\mathcal{E}$ on $X$, a flag refinement $f \colon Y_k \to X$ of $\mathcal{E}$ graded by the divisors $D_{\tau,i}$ of the toroidal flag space, an open $O \subseteq X$ and a Hermitian metric $h$ on $\mathcal{E}$ over $O$, such that:

1. $h$ is a Hermitian metric on $\mathcal{E}$ over $O$, and it is good;
2. for every weight $\lambda$ and every $R \in \mathbb{R}[c_{\tau,k}]$ with $\operatorname{antisym}(Q_{\lambda, \dim Y_k}) = \chi(R)\,\Delta$,
$$\int_O R(c(h)) = \operatorname{covol}(U_k) \cdot \deg_{\mathrm{Fl}}(\lambda).$$

Lean: `GlobalTheory.LieBase.exists_goodBase`.

*Proof.* Take a Lie base $X, j, f, \mathcal{E}, A_0$ for $Y_k$, with its graded flag refinement $f \colon Y_k \to X$. Let $O$ be its open part and $h$ its Hodge metric. The Hodge metric is smooth, Hermitian and positive definite on $O$, and compatible with the frames. It is good by the theorem that [the Hodge metric is good](/entry/lie-gram-is-good/). The integral is the theorem on [Chern integrals of the Hodge metric](/entry/has-chern-integral-covol-flag-deg/). $\square$

**Lemma 7.7.7 (Antisymmetric polynomials).** For every $Q \in \mathbb{R}[x_{\tau,i}]$ there is $R \in \mathbb{R}[c_{\tau,k}]$ with $\operatorname{antisym}(Q) = \chi(R)\,\Delta$.

*Proof.* The polynomial $\operatorname{antisym}(Q)$ changes sign under each transposition of two roots $x_{\tau,i}$ and $x_{\tau,j}$ with the same $\tau$. So it vanishes on $x_{\tau,i} = x_{\tau,j}$, and it is divisible by $x_{\tau,j} - x_{\tau,i}$. These factors are coprime, so $\Delta$ divides it. The quotient is symmetric in the roots of each $\tau$, and by the theorem on [symmetric polynomials](/learn/combinatorics/#symmetric-polynomials) it is $\chi(R)$ for some $R$. $\square$

**Lemma 7.7.8 (Self-intersection of the automorphic line bundle).** Let $L_\lambda = -\sum_{(\tau,i)} e_\lambda(\tau,i)\, D_{\tau,i}$ be the automorphic line bundle of weight $\lambda$ on $Y_k$. Then
$$\bigl(L_\lambda^{\dim Y_k}\bigr)_{Y_k} = I_D\bigl(Q_{\lambda, \dim Y_k}\bigr).$$

*Proof.* Expand $Q_{\lambda,d} = (-\sum e_\lambda(\tau,i)\, x_{\tau,i})^d$ into monomials of degree $d = \dim Y_k$. The intersection number $(L_\lambda^d)$ is multilinear in the $d$ factors, and expanding it gives the same coefficients. $\square$

**Theorem 7.7.9 (Mumford proportionality).** Assume good Chern-Weil theory. Let $\sigma$ satisfy `GoodEmb`, let $U$ satisfy `IsUnf`, let $\Phi$ be a toroidal flag space, let $k$ be a component and let $\lambda$ be a weight. Then
$$\bigl(L_\lambda^{\dim Y_k}\bigr)_{Y_k} = \operatorname{covol}(U_k) \cdot \deg_{\mathrm{Fl}}(\lambda).$$

Lean: `GlobalTheory.Proportionality.mumfordProportionality_of_goodChernWeil` (also `GlobalTheory.T.toroidalFlagProportionality_of_goodChernWeil`, a second name).

*Proof.* Put $d = \dim Y_k$. The [good base](/entry/exists-good-base/) gives $X$, $\mathcal{E}$, $f$, $O$ and a good metric $h$. The lemma on antisymmetric polynomials gives $R$ with $\operatorname{antisym}(Q_{\lambda,d}) = \chi(R)\,\Delta$. By the lemma on the self-intersection, the left side is $I_D(Q_{\lambda,d})$. By the proposition on Chern integrals as flag intersections, $\int_O R(c(h)) = I_D(Q_{\lambda,d})$. By the good base, $\int_O R(c(h)) = \operatorname{covol}(U_k)\, \deg_{\mathrm{Fl}}(\lambda)$. A Chern integral has only one value, so the two values are equal. $\square$

**Remark 7.7.10.** The theorem says that the degree of $L_\lambda$ on $Y_k$ is the degree of the corresponding line bundle on the flag variety of the compact dual, times the volume. The normalizations of $\operatorname{covol}$ in [the volume section](/entry/mass-open-part-eq-covol/) make the constant $1$. The case of the [abelian varieties](/learn/abelian-varieties/#mumfords-proportionality-theorem) with $\mathcal{O}_E$-action covers the unitary Shimura varieties of signature $(p, q)$.

**Remark 7.7.11 (Formalization).** Good Chern-Weil theory is `GoodChernWeil`, the conjunction of `GoodChernNumbers` and `FlagPushForward`, and the main statement is `MumfordProportionality`, all in [MumfordProportionality.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/MumfordProportionality.lean#L16). The proposition is `GoodChernWeil.flag` (line 33). `GoodChernNumbers` asks for no hypothesis on $X$ or on the boundary $X \setminus O$ beyond what `IsGood` and the type `Var` carry. The flag refinement is the structure `Refines` in ValRSpMapFromSpecStalk.lean, line 205, a file whose name does not describe it. The grading `IsGraded`, the intersection polynomial `interPoly` and the fibre point `fibrePoint` are in [InterPolyProdSum.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean#L23). The good base is in [ExistsGoodBase.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsGoodBase.lean#L15); its last step is `convert … using 3` (line 35). Another file with the same name, Proofs/InertiaEigenvalues/ExistsGoodBase.lean, is about a different subject. The two lemmas are `antisymm_eq_chernRoots_mul_rootDiscr` and `selfInter_Lw_interPoly`; we did not open their proofs, and the proofs above are ours. The main proof is in [ToroidalFlagProportionalityOfGoodChernWeil.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ToroidalFlagProportionalityOfGoodChernWeil.lean#L19). It ends with `convert key using 3 <;> exact Subsingleton.elim _ _` (line 26), which closes goals between instances. The second name is proved by `first | exact @…`, with `maxHeartbeats 1000000`. It is used by `Hypotheses2.toClassicalTheorems` and, through [the classical theorems](/entry/to-classical-theorems/), by the field `p16` of [the published results](/step/published-results-arithmetic/).

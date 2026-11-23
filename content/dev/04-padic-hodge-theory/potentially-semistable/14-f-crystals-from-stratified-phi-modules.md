---
title: F-crystals from stratified phi-modules and the coproduct prism
decls:
  - GlobalTheory.BSP.StratCrys.exists_crys
  - GlobalTheory.BSP.StratCrys.exists_framed
  - GlobalTheory.T.exists_framed_fCrystal_of_stratifiedPhiModule
  - GlobalTheory.BSP.nonempty_env
  - GlobalTheory.T.nonempty_breuilKisinPrismCoproduct
status: drafted
drafted_by: writer@claude-opus-5-5
---
## F-crystals from stratified phi-modules and the coproduct prism

This section proves two results used in the proof of Bhatt-Scholze integrality in the previous section. The first makes a prismatic F-crystal out of a stratified $\varphi$-module, with a frame at the Breuil-Kisin prism. This is the step from the matrices of a crystalline lattice to the F-crystal in [the Theorem on the standard prism](/entry/bhatt-scholze-integral/). The second constructs the coproduct of a prism $B$ with the Breuil-Kisin prism, when $I_B$ is principal and a lift of the uniformizer is given. Coproducts of this kind are the reason a descent datum $\varepsilon$ on the Breuil-Kisin prism determines a module on every prism. We keep the notation of the previous section: $\mathfrak{S} = W[[X]]$, the Eisenstein polynomial $E$, the Breuil-Kisin prism $(\mathfrak{S}, (E))$, and a stratified $\varphi$-module $S = (a', b, A, A', \varepsilon)$ of rank $d$. For a map $g$ from the Breuil-Kisin prism to a prism $B$, write $A^g$ for $A$ with $g$ applied to its entries.

**Definition 6.14.1 (Evaluation of a stratified module).** Let $B$ be a prism and $N$ a finite projective $B$-module. An *evaluation* of $S$ on $N$ gives, for each map of prisms $a : B \to Q$ and each map $g$ from the Breuil-Kisin prism to $Q$, a base change $v_{a,g} : N \to Q^d$ over $a$, such that:

1. $v_{a,g}(x) = \varepsilon(g, g')\,v_{a,g'}(x)$ for all $g, g'$;
2. $v_{c \circ a,\, c \circ g}(x) = c(v_{a,g}(x))$ for every map $c : Q \to Q'$.

For $t \in B$, a $\varphi$-semilinear map $\Psi : N \to N$ is a *Frobenius for $t$* if
$$g(E)^{a'}\,v_{a,g}(\Psi x) = a(t)^{a'}\,A^g\,\varphi(v_{a,g}(x))$$
for all $a$, $g$ and $x$.

Lean: `GlobalTheory.BSP.Eval` (also `GlobalTheory.BSP.IsPsi`, the Frobenius).

So $v_{a,g}$ is a trivialization of $N$ over $Q$ by means of $g$, and $\varepsilon$ is the change of trivialization. The Frobenius has matrix $A/E^{a'}$ in each trivialization, up to the factor $a(t)^{a'}$.

The next Lemma uses only the definition of a base change.

**Lemma 6.14.2 (Base change over the identity).** If an $A$-linear map $u : M \to N$ is a base change over the identity of $A$, then $u$ is bijective.

*Proof.* Apply the universal property to the identity of $M$. It gives an $A$-linear $w : N \to M$ with $w \circ u = \mathrm{id}_M$, so $u$ is injective. Then $(u \circ w) \circ u = u = \mathrm{id}_N \circ u$, and the uniqueness in the universal property, for the map $u$ itself, gives $u \circ w = \mathrm{id}_N$. So $u$ is surjective. $\square$

**Lemma 6.14.3 (F-crystal of a stratified module).** There are an F-crystal $M$ and, for every prism $B$, an evaluation $V_B$ of $S$ on $M(B)$, such that:

1. $V_{B'}$ and $V_B$ are compatible with the transition maps: $(V_{B'})_{a,g}(M(k)\,x) = (V_B)_{a \circ k,\, g}(x)$ for every map $k : B \to B'$;
2. for every prism $B$ and $t \in I_B$ there is a Frobenius $\Psi$ for $t$ on $M(B)$ with $\Phi_{B,t}(x) = \Psi(x)/t^{a'}$ for all $x$.

Lean: `GlobalTheory.BSP.StratCrys.exists_crys`.

*Proof.* The construction uses results proved elsewhere in this development. For each prism $B$ there is a finite projective $B$-module $N(B)$ with an evaluation $V_B$ of $S$. For each map $k : B \to B'$ there is a base change $t_k : N(B) \to N(B')$ over $k$ that is compatible with the evaluations as in 1. For each $t \in I_B$ there is a Frobenius $\Psi_{B,t}$ for $t$ on $N(B)$. Put $M(B) = N(B)$, $M(k) = t_k$ and $\Phi_{B,t} = \Psi_{B,t}/t^{a'}$.

The evaluations separate points: if $(V_B)_{a,g}(x) = (V_B)_{a,g}(y)$ for all $a$ and $g$, then $x = y$. Indeed, $B$ has a cover $h : B \to C$ by a prism $C$ that receives a map $f$ from the Breuil-Kisin prism, and $(V_B)_{h,f}$ is injective. By 1, both $M(\mathrm{id})$ and $\mathrm{id}$, and both $M(k' \circ k)$ and $M(k') \circ M(k)$, have the same evaluations, so $M$ is a functor. Each $\Phi_{B,t}$ is a base change: the linearization of $\Psi_{B,t}$ has kernel and cokernel killed by a power of $t$, so it becomes an isomorphism after $t$ is inverted. Naturality of $\Phi$ follows from the compatibility of $\Psi$ with the transition maps. Property 2 holds by definition. $\square$

**Theorem 6.14.4 (Framed F-crystal).** For every Breuil-Kisin datum and every stratified $\varphi$-module $S$ of rank $d$, there are an F-crystal $M$ and a basis $e_1, \dots, e_d$ of $M(\mathfrak{S}, (E))$ that is a frame of $M$ by $S$.

Lean: `GlobalTheory.BSP.StratCrys.exists_framed` (also `GlobalTheory.T.exists_framed_fCrystal_of_stratifiedPhiModule`, a second name).

*Proof.* Take $M$ and $V$ from the Lemma, and write $v_{a,g}$ for the maps of the evaluation $V_{\mathfrak{S}}$ at the Breuil-Kisin prism. The map $v_{\mathrm{id},\mathrm{id}} : M(\mathfrak{S}) \to \mathfrak{S}^d$ is a base change over the identity, so it is bijective by the first Lemma. Let $e_j$ be the preimage of the $j$-th unit vector $\delta_j$. For every map $g$ from the Breuil-Kisin prism to $B$, naturality gives $v_{g,g}(e_j) = g(v_{\mathrm{id},\mathrm{id}}(e_j)) = \delta_j$.

First condition of a frame. Let $f, g$ be maps from the Breuil-Kisin prism to $B$. By the compatibility 1 of the Lemma, $(V_B)_{\mathrm{id}, f}(M(g)\,x) = v_{g, f}(x)$ for $x \in M(\mathfrak{S})$. So
$$(V_B)_{\mathrm{id},f}(M(g)\,e_j) = v_{g,f}(e_j) = \varepsilon(f, g)\,v_{g,g}(e_j) = \varepsilon(f, g)\,\delta_j,$$
which is the $j$-th column of $\varepsilon(f, g)$, and $(V_B)_{\mathrm{id},f}(M(f)\,e_i) = v_{f,f}(e_i) = \delta_i$. Since $(V_B)_{\mathrm{id},f}$ is bijective and linear, $M(g)\,e_j = \sum_i \varepsilon(f, g)_{ij}\,M(f)\,e_i$.

Second condition. The element $E$ lies in the ideal $(E)$ of the Breuil-Kisin prism. Let $\Psi$ be the Frobenius for $E$ from the Lemma, with $\Phi_E(x) = \Psi(x)/E^{a'}$. With $a = g = \mathrm{id}$, the Frobenius identity gives $E^{a'}\,v_{\mathrm{id},\mathrm{id}}(\Psi e_j) = E^{a'}\,A\,\varphi(\delta_j) = E^{a'}\,A\,\delta_j$. The image of $E$ under any map from the Breuil-Kisin prism is a nonzero divisor, by a result proved elsewhere. So $v_{\mathrm{id},\mathrm{id}}(\Psi e_j)$ is the $j$-th column of $A$, and $\Psi(e_j) = \sum_i A_{ij}\,e_i$ since $v_{\mathrm{id},\mathrm{id}}$ is bijective. Hence $\Phi_E(e_j) = \big(\sum_i A_{ij} e_i\big)/E^{a'}$. $\square$

We turn to the coproduct. Let $X$ also denote the image of $X$ in $\mathcal{O}_K = \mathfrak{S}/(E)$, a uniformizer.

**Definition 6.14.5 (Frame of a prism and coproduct).** Let $B$ be a prism and $d, p \in B$. The pair $(d, p)$ is a *frame* of $B$ if $I_B = (d)$ and $p \bmod I_B$ is the image of the uniformizer $X$ under $\mathcal{O}_K \to B/I_B$. A *coproduct* of $B$ and the Breuil-Kisin prism along $(d, p)$ is a prism $Q$ with maps $i : B \to Q$ and $r$ from the Breuil-Kisin prism to $Q$, and an element $w \in Q$, such that:

1. for every prism $C$, every map $f : B \to C$ and every map $g$ from the Breuil-Kisin prism to $C$, there is a unique map $h : Q \to C$ with $h \circ i = f$ and $h \circ r = g$;
2. $r(X) = i(p) + i(d)\,w$ and $I_Q = (i(d))$;
3. $Q$ is topologically free over $B$, for the $(\ell) + I_B$-adic topology, on the monomials $\prod_k (\delta^k w)^{\alpha_k}$ with $0 \leq \alpha_k < \ell$ and almost all $\alpha_k = 0$.

Lean: `GlobalTheory.BSP.IsFrame` (also `GlobalTheory.BSP.Env`, the coproduct).

**Theorem 6.14.6 (Coproduct with the Breuil-Kisin prism).** For every Breuil-Kisin datum, every prism $B$ and every frame $(d, p)$ of $B$, a coproduct of $B$ and the Breuil-Kisin prism along $(d, p)$ exists.

Lean: `GlobalTheory.BSP.nonempty_env` (also `GlobalTheory.T.nonempty_breuilKisinPrismCoproduct`, a second name).

*Proof.* Let $J = (\ell) + I_B$. Since $I_B = (d)$ is the ideal of a prism, $\delta(d)$ is a unit, by a result proved elsewhere. The ideal $J$ is finitely generated, contains $\ell$ and $d$, and $B$ is $J$-adically complete. By a second result proved elsewhere there is a *$\delta$-envelope*: a $\delta$-ring $Q$ with a $\delta$-map $i : B \to Q$ and $w \in Q$ with $\delta(i(p) + i(d)\,w) = 0$, topologically free over $B$ on the monomials of property 3, and universal: for every $J'$-adically complete $\delta$-ring $C$, every $\delta$-map $f : B \to C$ with $f(J) \subseteq J'$ and every $v \in C$ with $\delta(f(p) + f(d)\,v) = 0$, there is a $\delta$-map $h : Q \to C$ with $h \circ i = f$ and $h(w) = v$.

The ring $Q$ with $I_Q = (i(d))$ is a prism. The basis shows that $i(d)$ is a nonzero divisor and that the $\ell$-power torsion of $Q/(i(d))$ is bounded by the bound for $B$. The ideal $(i(d))$ is invertible, $Q$ is complete, and $\ell \in I_Q + \varphi(I_Q)Q$ since $\delta(i(d))$ is a unit. The map $i$ is a map of prisms, and $(i(d),\, i(p) + i(d)\,w)$ is a frame of $Q$. Since $\delta(i(p) + i(d)\,w) = 0$, there is a map $r$ from the Breuil-Kisin prism to $Q$ with $r(X) = i(p) + i(d)\,w$. This gives property 2.

For property 1, let $f : B \to C$ and $g$ be given. Then $I_C = (f(d))$, and $f(d)$ is a nonzero divisor. The image $g(X)$ satisfies $\delta(g(X)) = 0$ and lifts the uniformizer, so $g(X) \equiv f(p) \bmod f(d)$. Write $g(X) = f(p) + f(d)\,v$. Then $\delta(f(p) + f(d)\,v) = 0$, and the universal property of the envelope gives $h$ with $h \circ i = f$ and $h(w) = v$. This $h$ is a map of prisms. Then $h(r(X)) = f(p) + f(d)\,v = g(X)$, and a map from the Breuil-Kisin prism is fixed by the image of $X$, so $h \circ r = g$. For uniqueness, let $h'$ also satisfy both equations. Then $f(p) + f(d)\,h'(w) = h'(r(X)) = g(X) = f(p) + f(d)\,v$, and since $f(d)$ is a nonzero divisor, $h'(w) = v$. A $\delta$-map out of $Q$ is fixed by its composite with $i$ and its value at $w$, by the topological basis, so $h' = h$. $\square$

**Remark 6.14.7 (Formalization).** The steps in the proof of the Lemma are `GlobalTheory.T.exists_stratifiedPhiModuleValue`, `GlobalTheory.T.exists_stratifiedValue_transition_baseChange`, `GlobalTheory.T.exists_frobenius_on_stratifiedValue`, `GlobalTheory.T.exists_prism_cover_receiving_breuilKisin` with `GlobalTheory.T.injective_and_range_of_prism_cover` (in `eval_ext`), `GlobalTheory.T.linearizedFrobenius_invertible_up_to_pow` with `GlobalTheory.T.isSemilinearBaseChange_localized_of_torsion_bounded` (in `semiBC_fracMap`), and `GlobalTheory.T.isLocalizedFraction_semilinear_transition` with `GlobalTheory.T.stratifiedValue_frobenius_comm_transition`; we read their statements, not their proofs. The nonzero divisor fact is `GlobalTheory.T.breuilKisinHom_eisenstein_span_and_nonZeroDivisor`. In the Theorem on the coproduct, the envelope is `GlobalTheory.T.nonempty_envRing`, of type `EnvRing`, and the other steps are `GlobalTheory.T.isUnit_delta_of_prism_ideal_eq_span`, `GlobalTheory.T.regular_and_bounded_torsion_of_adicTopologicalBasis`, `GlobalTheory.T.exists_breuilKisinHom_of_uniformizerFrame`, `GlobalTheory.T.breuilKisinHom_image_X_delta_zero_lifts_uniformizer`, `GlobalTheory.T.prism_hom_map_ideal_eq`, `GlobalTheory.T.breuilKisin_prism_hom_ext_of_X` and `GlobalTheory.T.deltaRingHom_unique_of_adicTopologicalBasis`. The proof is in [NonemptyBreuilKisinPrismCoproduct.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/NonemptyBreuilKisinPrismCoproduct.lean#L231); the universal property `EnvCop.univ` at [line 180](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/NonemptyBreuilKisinPrismCoproduct.lean#L180) runs under `maxHeartbeats 2000000`. The topological basis is the structure `TopBasis` with coefficient maps, finiteness modulo powers of $J$ and approximation; "topologically free" above stands for it. Both second names are proved by `first | exact ...` under `maxHeartbeats 1000000`. The Lemma is stated with `variable (S) in` and takes the Breuil-Kisin datum as an implicit argument, while the Theorem on frames takes all its arguments explicitly.

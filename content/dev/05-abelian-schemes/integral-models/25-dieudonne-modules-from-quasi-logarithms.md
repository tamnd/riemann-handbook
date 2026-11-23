---
title: Dieudonné modules from quasi-logarithms
decls:
  - GlobalTheory.Katz.reductionMap
  - GlobalTheory.exists_base_isConn_katz
  - GlobalTheory.T.exists_connected_dieudonne_functor_quasiLogarithms
  - GlobalTheory.Dieu.theory
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Dieudonné modules from quasi-logarithms

The next section computes characteristic polynomials of endomorphisms on [algebraic de Rham cohomology|13F5JZPDD0] in characteristic $p$ through a Dieudonné module, which this section sets up. A Dieudonné theory is a contravariant functor from $p$-divisible groups over perfect fields to free modules of finite rank over the Witt vectors, with a Frobenius, a Verschiebung and a reduction modulo $p$ onto rigidified extensions. We build it on connected groups by the method of Katz, from quasi-logarithms of formal group laws, and we fix one theory by choice.

Throughout, $p$ is a prime, $k$ is a perfect field of characteristic $p$, $W = W(k)$ is its ring of Witt vectors and $K$ is the fraction field of $W$. For a series $f$ over $k$ we write $[f]$ for the series over $K$ whose coefficients are the Teichmüller lifts of those of $f$.

### $p$-divisible groups

**Definition 8.25.1 ($p$-divisible group).** A *$p$-divisible group* $G$ of height $h$ over a ring $O$ is a sequence of commutative and cocommutative Hopf algebras $A_n(G)$ over $O$, each [finite|N9C4X7XKE4] and projective of rank $p^{nh}$, with surjective maps $A_{n+1}(G) \to A_n(G)$ of algebras and coalgebras whose kernel is the ideal of $p^n$-torsion. A morphism $G \to H$ is a compatible family of Hopf algebra maps $A_n(H) \to A_n(G)$. The group $G$ is *connected* if every element of the augmentation ideal of each $A_n(G)$ is nilpotent, and *étale* if each $A_n(G)$ is reduced. For a ring map $\sigma : O \to O'$, a *semilinear map* $s$ from a group $G'$ over $O'$ to a group $G$ over $O$ is a compatible family of $\sigma$-semilinear bialgebra maps $s_n : A_n(G) \to A_n(G')$. The *absolute Frobenius* of $G$ over $k$ is the semilinear map over the Frobenius of $k$ given by $a \mapsto a^p$.

Lean: `GlobalTheory.PDivGroup`, `GlobalTheory.PDivGroup.IsConn`, `GlobalTheory.PDivGroup.IsEt`, `GlobalTheory.PDivGroup.SemiHom`.

Each $G$ over $k$ has a $k$-space $\operatorname{RigExt}(G)$ of *rigidified extensions*: pairs of compatible 2-cocycles and invariant differentials, modulo the pairs coming from functions. A semilinear map $s$ over $\sigma$ induces a $\sigma$-semilinear map $s_{\mathrm{rig}} : \operatorname{RigExt}(G) \to \operatorname{RigExt}(G')$.

Lean: `GlobalTheory.PDivGroup.RigExt`, `GlobalTheory.PDivGroup.SemiHom.rig`.

### Dieudonné bases and theories

**Definition 8.25.2 (Dieudonné base).** Let $\mathcal{P}$ be a property of $p$-divisible groups. A *Dieudonné base* $B$ on $\mathcal{P}$ assigns to each perfect field $k$ of characteristic $p$ and each $G$ over $k$ with property $\mathcal{P}$ a $W$-module $M(G)$, free and finite, and to each semilinear map $s$ over $\sigma : k \to k'$ from $G'$ to $G$ an additive map $s^* : M(G) \to M(G')$, with the following properties.

1. $s^*(a m) = W(\sigma)(a)\, s^*(m)$ for $a \in W$.
2. The identity of $G$ gives the identity, and $(f + g)^* = f^* + g^*$ for morphisms $f, g : G \to H$.
3. If $u$ is the composite of $s$ and $t$, then $u^* = t^* \circ s^*$.
4. There is a map $\mathrm{red} : M(G) \to \operatorname{RigExt}(G)$, semilinear over $W \to k$, which is surjective, with $\mathrm{red}(m) = 0$ if and only if $m \in pM(G)$, and with $\mathrm{red}(s^* m) = s_{\mathrm{rig}}(\mathrm{red}\, m)$.

So $f : G \to H$ over $k$ gives a $W$-linear $f^* : M(H) \to M(G)$, and the absolute Frobenius gives a Frobenius-semilinear $F : M(G) \to M(G)$.

Lean: `GlobalTheory.Dieu.Base` (with `GlobalTheory.Dieu.Base.map` and `GlobalTheory.Dieu.Base.F`).

**Definition 8.25.3 (Formal group law, quasi-logarithm).** Let $X = (X_1, \dots, X_d)$ and $Y = (Y_1, \dots, Y_d)$. A *formal group law* of dimension $d$ over $k$ is a tuple $\mu$ of series in $k[[X, Y]]$ with zero constant terms such that $\mu(X, 0) = X$, $\mu(X, Y) = \mu(Y, X)$ and $\mu(\mu(X, Y), Z) = \mu(X, \mu(Y, Z))$. For a series $f$ in $d$ variables, its *coboundary* is
$$\delta_\mu f = f(\mu(X, Y)) - f(X) - f(Y),$$
and $\operatorname{lin}(f) \in k^d$ is the vector of its coefficients of $X_1, \dots, X_d$. A series $c(X, Y)$ is a *symmetric 2-cocycle* if $c(Y, X) = c(X, Y)$ and
$$c(Y, Z) - c(\mu(X, Y), Z) + c(X, \mu(Y, Z)) - c(X, Y) = 0.$$
A series $f \in K[[X]]$ is *integral* if its coefficients lie in $W$, and *quasi-integral* if $\alpha_i a_\alpha \in W$ for each coefficient $a_\alpha$ of $X^\alpha$ and each $i$. A *quasi-logarithm* of $\mu$ is a quasi-integral $f \in K[[X]]$ such that $\delta_{[\mu]} f$ is integral. The quasi-logarithms form a $W$-module, and the *Katz module* is
$$\operatorname{Mod}(\mu) = \{\text{quasi-logarithms}\} / \{\text{integral quasi-logarithms}\}.$$
An integral series $f$ over $K$ *reduces to* a series $g$ over $k$ if each coefficient of $g$ is the image of that of $f$; the same is said of vectors.

Lean: `GlobalTheory.Katz.IsLaw`, `GlobalTheory.Katz.cob1`, `GlobalTheory.Katz.lin`, `GlobalTheory.Katz.IsCoc`, `GlobalTheory.Katz.quasiLog`, `GlobalTheory.Katz.Mod`, `GlobalTheory.Katz.Red`, `GlobalTheory.Katz.RedV`.

**Definition 8.25.4 (Chart).** A *chart* of dimension $d$ of $G$ over $k$ is a family of nilpotent elements $x_{n,1}, \dots, x_{n,d}$ of $A_n(G)$ with counit $0$, compatible with the maps $A_{n+1}(G) \to A_n(G)$, such that evaluation at $x_n$ maps $k[[X]]$ onto $A_n(G)$, with kernel in degrees above any bound once $n$ is large. The chart is *for* a law $\mu$ if the comultiplication sends $x_{n,i}$ to $\mu_i$ evaluated at $(x_n \otimes 1, 1 \otimes x_n)$. A tuple $\varphi$ of series in $d$ variables *gives* a morphism $f : G \to H$ in charts $c$ of $G$ and $c'$ of $H$ if $f_n(x'_{n,j})$ is $\varphi_j$ evaluated at $x_n$.

Lean: `GlobalTheory.Katz.Chart`, `GlobalTheory.Katz.Chart.IsLawOf`, `GlobalTheory.Katz.Chart.IsMapOf`.

**Definition 8.25.5 (Katz property).** A base $B$ on $\mathcal{P}$ has the *Katz property* if for each $G$ with property $\mathcal{P}$ and each chart $c$ of $G$ for a law $\mu$ there is a $W$-linear isomorphism $e_c : M(G) \cong \operatorname{Mod}(\mu)$ with the following properties.

1. For every quasi-logarithm $f$, the transport of $F$ by $e_c$ sends the class of $f$ to the class of $f^\sigma(X_1^p, \dots, X_d^p)$, where $f^\sigma$ applies the Frobenius of $K$ to the coefficients.
2. If $c'$ is a chart of $H$ for a law $\nu$ and $\varphi$, with zero constant terms, gives $f : G \to H$ in $c$ and $c'$, then the transport of $f^*$ by $e_c$ and $e_{c'}$ sends the class of $g$ to the class of $g([\varphi])$.

Lean: `GlobalTheory.Dieu.Base.Katz` (with `GlobalTheory.KatzF.IsF` and `GlobalTheory.KatzF.IsPull`).

**Definition 8.25.6 (Dieudonné theory).** A *Dieudonné theory* is a base $B$ on all $p$-divisible groups with the Katz property and with a map $V : M(G) \to M(G)$, semilinear for the inverse of the Frobenius of $W$, such that $FV = VF = p$, and with a duality for étale groups: for étale $G$ an isomorphism $e$ of $M(G)$ with the $W$-dual of $M(G^\vee)$ for the Cartier dual $G^\vee$, natural in $G$, with $e(Fx)(Fy) = p \cdot \operatorname{Frob}(e(x)(y))$.

Lean: `GlobalTheory.Dieu.Theory` (with `GlobalTheory.Dieu.Base.EtDual`).

### The reduction map

**Theorem 8.25.7 (Reduction map).** Let $\mu$ be a formal group law of dimension $d$ over $k$, $V$ a $k$-vector space and $\rho : k[[X, Y]] \times k^d \to V$ a $k$-linear map such that every $v \in V$ is $\rho(c, w)$ for a symmetric 2-cocycle $c$, and such that for a symmetric 2-cocycle $c$ we have $\rho(c, w) = 0$ if and only if $c = \delta_\mu b$ and $w = \operatorname{lin}(b)$ for some $b \in k[[X]]$. Then there is a map $r : \operatorname{Mod}(\mu) \to V$, semilinear over $W \to k$, such that:

1. if $f$ is a quasi-logarithm, $\delta_{[\mu]} f$ reduces to $c$ and $\operatorname{lin}(f)$ reduces to $w$, then $r[f] = \rho(c, w)$;
2. $r$ is surjective;
3. $r(m) = 0$ if and only if $m \in p \operatorname{Mod}(\mu)$.

Lean: `GlobalTheory.Katz.reductionMap`.

We use the following results.

### Inputs

1. A series over $K$ is integral if and only if it reduces to some series over $k$; that series is unique; $[g]$ reduces to $g$; and reduction respects sums, differences and multiplication by $a \in W$, where $a$ acts on the reduction through its image in $k$. (`GlobalTheory.T.mvPowerSeries_reduction_mod_prime_rules`)
2. If $b$ reduces to $b'$, then $\delta_{[\mu]} b$ reduces to $\delta_\mu b'$ and $\operatorname{lin}(b)$ reduces to $\operatorname{lin}(b')$. (`GlobalTheory.T.reduction_commutes_formalGroupLawCoboundaries`)
3. For a quasi-logarithm $f$, the series $\delta_{[\mu]} f$ and the vector $\operatorname{lin}(f)$ reduce to some $c$ and $w$, and every such $c$ is a symmetric 2-cocycle. (`GlobalTheory.T.quasiLog_reduces_to_cocycle`)
4. If $f$ is a quasi-logarithm, $\delta_{[\mu]} f$ reduces to $\delta_\mu b$ and $\operatorname{lin}(f)$ reduces to $\operatorname{lin}(b)$, then $f - pg$ is integral for some quasi-logarithm $g$. (`GlobalTheory.T.quasiLogarithm_eq_p_smul_add_integral`)
5. For each symmetric 2-cocycle $c$ and each $w \in k^d$ there is a quasi-logarithm $f$ such that $\delta_{[\mu]} f$ reduces to $c$ and $\operatorname{lin}(f)$ reduces to $w$. (`GlobalTheory.T.exists_quasiLog_red_coboundary_and_linear`)

*Proof.* For a quasi-logarithm $f$, result 3 gives reductions $c_f$ and $w_f$; put $\Phi(f) = \rho(c_f, w_f)$, which by result 1 does not depend on the choice. Since $[\mu]$ has zero constant terms, $\delta_{[\mu]}$ is additive and $W$-linear, so result 1 shows that $\Phi$ is additive and semilinear over $W \to k$. If $f$ is integral, it reduces to some $b$ by result 1, so $c_f = \delta_\mu b$ and $w_f = \operatorname{lin}(b)$ by result 2, and $\Phi(f) = 0$ by the hypothesis on $\rho$. Hence $\Phi$ factors through a map $r$ on $\operatorname{Mod}(\mu)$, and claim 1 holds. For claim 2, write $v = \rho(c, w)$ with $c$ a symmetric 2-cocycle and take $f$ from result 5. For claim 3, if $r[f] = 0$ then $c_f$ is a cocycle by result 3, so $c_f = \delta_\mu b$ and $w_f = \operatorname{lin}(b)$ for some $b$, and result 4 gives $g$ with $[f] = p[g]$. Conversely $r(pm) = p\, r(m) = 0$ since $p = 0$ in $k$. $\square$

### The connected base

**Theorem 8.25.8 (Connected Dieudonné base).** There is a Dieudonné base on connected $p$-divisible groups with the Katz property.

Lean: `GlobalTheory.exists_base_isConn_katz` (also `GlobalTheory.T.exists_connected_dieudonne_functor_quasiLogarithms`, a second name).

We use the following results, with $\sigma : k \to k'$.

### Inputs

1. A connected $G$ over a field in which $p = 0$ has a chart of some dimension $d$. (`GlobalTheory.T.exists_connectedPDivGroupChart_of_isConn`)
2. Each chart is a chart for some $\mu$, and each such $\mu$ is a formal group law. (`GlobalTheory.T.connectedPDivGroup_formalLaw_coordinates`, `GlobalTheory.T.isCommFormalGroupLaw_of_isLawOf`)
3. For a chart $c$ of $G$ there is a $k$-linear $\rho_c : k[[X, Y]] \times k^d \to \operatorname{RigExt}(G)$ sending $(t, w)$ to the class of the cocycles $t(x_n \otimes 1, 1 \otimes x_n)$ and the differentials $\sum_i w_i\, dx_{n,i}$. If $c$ is for $\mu$, every such map satisfies the hypotheses of the reduction theorem. (`GlobalTheory.T.exists_rigidifiedExtension_of_series_pair`, `GlobalTheory.T.rigidifiedExtension_presentation_of_series_pairs`)
4. For charts $c$ of $G$ and $c'$ of $G'$ and a semilinear map $s$ over $\sigma$ from $G'$ to $G$, there is a unique tuple $\varphi$ of series over $k'$ with $s_n(x_{n,j})$ equal to $\varphi_j$ evaluated at $x'_n$, and if $c$ is for $\mu$ and $c'$ is for $\nu$, then $\varphi$ is a homomorphism from $\mu^\sigma$ to $\nu$. (`GlobalTheory.T.existsUnique_powerSeries_semilinear_pDivGroupHom_chart`, `GlobalTheory.T.connectedPDivGroupChart_semilinearHom_isFormalGroupHom`)
5. If $\varphi$ is a homomorphism from $\mu^\sigma$ to $\nu$, there is a map $\operatorname{Mod}(\mu) \to \operatorname{Mod}(\nu)$, semilinear over $W(\sigma)$, sending the class of $f$ to the class of $f^\sigma([\varphi])$. (`GlobalTheory.T.map_formalGroupLawQuasiLogarithms`, `GlobalTheory.Katz.ModHom.map_exists`)
6. For a quasi-logarithm $f$ of $\nu$ we have $f([X]) = f$, and for series $\varphi$ and $\psi$ with zero constant terms the series $f([\psi(\varphi)]) - f([\psi])([\varphi])$ and $f([\nu(\varphi, \psi)]) - f([\varphi]) - f([\psi])$ are integral. (`GlobalTheory.Katz.PullQuasiLog.main`)
7. If $\varphi$ and $\psi$ give $f$ and $g$ in charts $c$ and $c'$, where $c'$ is for $\nu$, then $\nu(\varphi, \psi)$ gives $f + g$. (`GlobalTheory.T.isMapOf_add_formalGroupLawEvalPoints`)
8. The maps $\rho$ of result 3 are compatible with semilinear maps: $\rho_{c'}$ of the pullback of $(t, w)$ along $\varphi^\sigma$ equals $s_{\mathrm{rig}}(\rho_c(t, w))$ for a cocycle $t$. (`GlobalTheory.T.rigidifiedExtension_presentation_natural_semilinear`)
9. $\operatorname{RigExt}(G)$ is finite dimensional; if $c$ is for $\mu$, then $\operatorname{Mod}(\mu)$ is $p$-adically separated without $p$-torsion; and such a $W$-module $M$ with a surjection as in the reduction theorem onto a finite dimensional space, with kernel in $pM$, is free and finite. (`GlobalTheory.PDivGroup.finrank_rigExt_omega`, `GlobalTheory.T.eq_zero_of_formalGroupLawCoboundaryOne_eq_zero`, `GlobalTheory.Katz.mod_noPTorsion`, `GlobalTheory.Katz.WittHaus.haus`, `GlobalTheory.wittModule_free_finite_of_reduction`)

*Proof.* For each connected $G$ choose a chart $c_G$ for a law $\mu_G$ (results 1 and 2), a map $\rho_G$ (result 3) and a reduction map $r_G$ from the reduction theorem, and put $M(G) = \operatorname{Mod}(\mu_G)$ and $\mathrm{red} = r_G$. For any charts $c$ of $G$ and $c'$ of $G'$ and any $s$, call a map $m : \operatorname{Mod}(\mu) \to \operatorname{Mod}(\nu)$ a *chart pull* if it sends the class of $f$ to the class of $f^\sigma([\varphi])$ for the tuple $\varphi$ of result 4. Results 4 and 5 give a semilinear chart pull, and we let $s^*$ be the chart pull for $c_G$ and $c_{G'}$. By result 9, $M(G)$ is free and finite, and the reduction theorem gives surjectivity and the kernel.

The other axioms are checked on classes. For the identity $\varphi = X$ and result 6 applies. For a composite, result 4 identifies its series with the composite of the series, and result 6 compares the chart pulls modulo integral series. For a sum, result 7 gives the series $\nu(\varphi, \psi)$, and result 6 again applies. The compatibility of $\mathrm{red}$ with $s^*$ follows from claim 1 of the reduction theorem and result 8.

For the Katz property, let $e_c$ be the chart pull of the identity from $c_G$ to a chart $c$ for $\mu$; the pull back is its inverse. The absolute Frobenius has series $X_j^p$, since $x_{n,j}^p$ is $X_j^p$ evaluated at $x_n$, and $f^\sigma([X^p]) = f^\sigma(X_1^p, \dots, X_d^p)$; with the composite rule this gives condition 1. For condition 2 the series of $f$ is $\varphi$ itself, and the composite rule gives the claim. $\square$

### The chosen theory

**Definition 8.25.9 (The Dieudonné theory).** For each prime $p$ we fix one Dieudonné theory: the theory formed from choices of the following data, each provided by the result named.

1. A base $B_c$ on connected groups with the Katz property, by the theorem above.
2. A base $B_e$ on étale groups with an étale duality to $B_c$: for étale $G$, $M_e(G)$ is the $W$-dual of $M_c(G^\vee)$, compatibly with $F$ and with morphisms as in the definition of a theory. (`GlobalTheory.T.exists_etaleDieudonneBase_by_cartierDuality`)
3. From $B_c$ with the Katz property and $B_e$ with this duality, a base on all groups with the Katz property and with étale duality to itself. (`GlobalTheory.T.exists_dieudonneFunctor_glued_connected_etale`)
4. For a base on all groups, a Verschiebung $V$ with $FV = VF = p$. (`GlobalTheory.T.exists_verschiebung_of_dieudonneFunctorBase`)

Lean: `GlobalTheory.Dieu.theory`.

It is used in [the next section](/entry/charpoly-push/).

**Remark 8.25.10 (Formalization).** The reduction theorem is in [ReductionMap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReductionMap.lean#L13). The connected base is in [ExistsConnectedDieudonneFunctorQuasiLogarithms.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsConnectedDieudonneFunctorQuasiLogarithms.lean#L256), with the chart pulls as lemmas of the same file from [line 40](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsConnectedDieudonneFunctorQuasiLogarithms.lean#L40) on. The second name is a wrapper under a raised heartbeat limit that tries three tactics: [ExistsConnectedDieudonneFunctorQuasiLogarithmsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsConnectedDieudonneFunctorQuasiLogarithmsStatement.lean#L7). Bases and theories are defined in [RedSurjective.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RedSurjective.lean#L38) and the Katz module in [FormalCoboundarySmul.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FormalCoboundarySmul.lean#L163). The chosen theory is in [FinrankTheoryMu.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FinrankTheoryMu.lean#L16); it is defined by choice, and the file name does not match its content. The maps $s^*$ of a base go from $M(G)$ to $M(G')$ for a map from $G'$ to $G$, so the functor is contravariant. In condition 2 of the Katz property the series $\varphi$ are assumed to have zero constant terms, but the proof does not use this assumption. We have not unfolded $\operatorname{RigExt}$ or the Cartier dual beyond the description above. We read the statements of the results quoted in this section, not their proofs.

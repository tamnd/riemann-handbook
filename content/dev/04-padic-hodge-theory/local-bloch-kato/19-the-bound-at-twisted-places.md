---
title: The bound at twisted places
decls:
  - GlobalTheory.TwistedPlaceBound.closing
  - GlobalTheory.T.twistedPlace_selmerLengthBound_of_localDuality
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The bound at twisted places

This section proves three facts about the twisted places of the series over the two special primes $q$ and $d$ of the host field. The first two describe the local fields and the action of the decomposition and inertia groups on the CM type. The third bounds the congruence valuation at a twisted localisation over $q$ or $d$ by an explicit quantity. The proof applies the theorem on admitted hypotheses for the bound to [Theorem A](/entry/theorem-a-closing/) with constant $160$ and to the local inputs of the chapter. The result is used where the series bounds its congruence lengths at twisted places.

We keep the notation of Section 9. Let $D$ be the data of the series. Its host field $E$ is a number field with a complex conjugation $c$ and a CM type $\Phi$, a set of embeddings $E \to \mathbb{C}$, and the data fix two primes $q$ and $d$. The data have numbers $f$, $r$, $t$ and $m$, and size data with numbers $b$, $S_c$, $\eta$, $x$ and $C_t$. A localisation $i$ has a prime $\ell_i$, a place $w_i$, the set $Z^{\mathrm{good}}_i$ of good eigensystems, and for each $\pi \in Z^{\mathrm{good}}_i$ a *congruence valuation* $v_{\mathrm{cc}}(i, \pi)$. For each place $w$ of $E$ over $\ell_i$ the data give a finite extension $K_w$ of $\mathbb{Q}_{\ell_i}$ with maximal unramified subfield $K_{w,0}$, and $K_{w,1}$ is the field of level $1$ over $K_{w,0}$, as in Section 17. We do not unfold the congruence valuation, the field of level $1$, or the numbers $h_E$, $s_\pi$ and $\mathrm{sha}(\ell, e)$ below.

**Definition 7.19.1 (The bound $B_C$).** For a real $C$, a polynomial $P$ in three variables with natural coefficients, and a prime $\ell$, put
$$B_C(\ell) = C f\Big(r\Big(\frac{b}{\ell} + S_c + t + \eta + \log b\Big) + m b\Big) + P(f, r, t) \log b.$$

**Definition 7.19.2 (The three conclusions).** The *local fields* conclusion says: for each localisation $i$ with $\ell = \ell_i \in \{q, d\}$ and each place $w$ of $E$ over $\ell$,

1. there is $y$ with $y^2 = -\ell$ and $K_w = K_{w,0}(y)$;
2. $K_w \subseteq K_{w,1}$ and $[K_w : K_{w,0}] = 2$;
3. $[K_{w,1} : \mathbb{Q}_\ell] = \frac{\ell - 1}{2} [K_w : \mathbb{Q}_\ell]$.

The *decomposition* conclusion says: for $\ell \in \{q, d\}$, $\ell \equiv 3 \pmod 4$, and every place $v$ of $E$ over $\ell$ has ramification index $2$ and satisfies $c\, v \ne v$. Also:

1. if $\ell = q$, every $\sigma$ in the decomposition group of $v$ preserves $\Phi$: $\varphi \circ \sigma \in \Phi$ if and only if $\varphi \in \Phi$;
2. if $\ell = d$, every $\sigma \ne 1$ in the inertia group of $v$ sends $\Phi$ to its complement: $\varphi \circ \sigma \in \Phi$ if and only if $\varphi \notin \Phi$.

The *valuation bound* with constant $C$ and polynomial $P$ says: let $i$ be a localisation with $\ell = \ell_i \in \{q, d\}$ and $w_i$ twisted, and assume $x^{2C_t + 5} < \ell$. Let $\pi \in Z^{\mathrm{good}}_i$ satisfy the finiteness condition $s_{\mathrm{fin}}$, and assume that the Tate-Shafarevich lengths of the local data at $\ell$ are finite in degrees $0 < e < t$. Then
$$v_{\mathrm{cc}}(i, \pi) \le B_C(\ell) + \sum_{0 < e < t} \mathrm{sha}(\ell, e) + v_\ell(h_E) + s_\pi + \frac{1}{\ell^2}.$$

**Theorem 7.19.3 (The bound at twisted places).** Assume global Artin reciprocity, the Bloch-Kato dimension formula, local Tate duality and the local Euler characteristic formula. Let $D$ be the data of the series and $H$, $F$, $C_m$ local data over $D$. Let $r$ and $\rho$ be families of global representations at the localisations, fix size data, a sign $\epsilon$, a real $C \ge 2080$, and a polynomial $P$ in three variables with natural coefficients such that $260 f^2 t^2 (r + t) \le P(f, r, t)$ for all $f, r, t$. Assume the global hypotheses on $r$ and $\rho$: the global index away from types, six global admitted statements, the Iwahori admissible set, the killing of twisted places, Hodge-Tate windows at the distinguished primes for $\epsilon$, the Fontaine condition on sums at the distinguished primes, the tame generator conditions at each localisation over $q$ or $d$ with a twisted place, and the polynomial bound on the parameters. Then the local fields conclusion, the decomposition conclusion, and the valuation bound with constant $C$ and polynomial $P$ hold.

Lean: `GlobalTheory.TwistedPlaceBound.closing` (also `GlobalTheory.T.twistedPlace_selmerLengthBound_of_localDuality`, a second name).

*Proof.* We collect the admitted statements of the bound one at a time.

*Step 1: Wach modules.* The used forms of the local conclusions on Wach modules hold for the local data. With them and the crystalline condition at all places, a theorem on Wach hypotheses gives the Wach statement for crystalline lattices at every place over a localisation, at level $1$.

*Step 2: Theorem A.* By [Theorem A](/entry/theorem-a-closing/), with the three published local inputs, Theorem A with constant $160$ holds for the local data.

*Step 3: the local theorem on lengths.* By [the theorem from local duality](/entry/theorem-tb-of-local-bloch-kato-duality-euler/), the local inputs give a statement on the lengths of local cohomology for the local data. A second theorem gives the Bloch-Kato formula at all places from local Tate duality and the Euler characteristic formula.

*Step 4: the literature hypotheses.* At each localisation $i$ over $q$ or $d$ with a twisted place, the literature hypotheses hold:

1. the tame generator conditions, which are a hypothesis;
2. at each place $w$ over $\ell_i$, Tate duality for $H^2$ with all coefficients, from local Tate duality at $K_w$ and the integers of the coefficient field, and the Bloch-Kato dimension at the auxiliary places, from local Tate duality and the Euler characteristic formula;
3. the compatibility of local coefficients through the tie;
4. the Fontaine properties at all places;
5. Tate duality for the top $H^2$ in integral form, from local Tate duality;
6. a bound for the unramified class field, from global Artin reciprocity.

*Step 5: the local fields.* A theorem on the local fields at the auxiliary primes gives the local fields conclusion and the decomposition conclusion. It uses none of the published inputs.

*Step 6: the bound.* Since $13 \cdot \max(160, 0) = 2080 \le C$, the theorem on admitted hypotheses for the bound applies with the constant $160$ of Theorem A, the polynomial $P$, the statements of Steps 1 to 4, and the global hypotheses. It gives the valuation bound with constant $C$ and polynomial $P$. $\square$

Global Artin reciprocity enters only in item 6 of Step 4. The sign $\epsilon$ enters only through the hypothesis on Hodge-Tate windows, which is passed to the theorem of Step 6 without change.

**Remark 7.19.4 (Formalization).** The three conclusions are `EmbeddingTypeJumps.Conclusion0`, `Conclusion1` and `Conclusion2` ([EmbeddingTypeJumps.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/EmbeddingTypeJumps.lean#L262), lines 29 and 65), and $B_C$ is `bndB` (line 45). The second name says "Selmer length bound", but the main conclusion bounds the congruence valuation `vcc`. In `Conclusion2` the finiteness hypothesis uses `Formalism.GaloisCohomology.shaLen` of the local data, while the bound uses the field `D.what₂.shaLen`, a separate function $\mathbb{N} \to \mathbb{N} \to \mathbb{Q}$ in the data ([DataRows.lean](lean:Formalism/LocalRingCardinality/DataRows.lean#L166)); no lemma in this proof ties the two. The steps are `GlobalTheory.T.wachModuleLocalConclusions_usedForms` and `GlobalTheory.T.wachHypothesis_crystallineLattices` (Step 1), `GlobalTheory.T.localLifting_of_blochKato_tateDuality_eulerChar` at $160$ (Step 2), `GlobalTheory.T.theorem_tb_of_local_blochKato_duality_euler` and `GlobalTheory.T.blochKatoLocal_all_of_tateDuality_eulerChar` (Step 3), `GlobalTheory.T.unramifiedClassFieldBound_of_artin` among others (Step 4), `GlobalTheory.T.local_fields_at_auxiliary_primes` (Step 5) and `GlobalTheory.T.theoremB_of_admittedHypotheses` (Step 6), which we read only through their statements ([TwistedPlaceSelmerLengthBoundOfLocalDuality.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedPlaceSelmerLengthBoundOfLocalDuality.lean#L28)). The arguments `HW`, `F` and `Cm` of the statement do not occur in its conclusion. The second name is a one-line wrapper.

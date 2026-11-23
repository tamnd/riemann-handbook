---
title: Positive step scalars
decls:
  - GlobalTheory.T.thetaChainStep_positive_scalar_standingHypotheses
  - GlobalTheory.Core.Rk.ScalarsRow.scalars
  - GlobalTheory.Core.Rk.ScalarsRow.scalars_of_heckeFormNS
  - GlobalTheory.T.thetaChain_steps_positive_multiple_of_LValue
  - GlobalTheory.ChainTw.scalars_of_given_all
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Positive step scalars

This section proves the scalar law of a theta chain: each step of the chain multiplies inner products by a positive constant times a value of a partial $L$-function. The constant depends on the step but not on the row of the chain. The proof puts together the [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula), which is a published hypothesis, [the peeling of the twist places](/entry/q-peel-holds/), [the Hecke parameters along the chain](/entry/up-q-holds/), and several facts about the stages proved in other chapters. The scalar law is used in [the next section](/entry/up-inj/) to prove that the up maps of the chain are injective, and from there in [the theorem on large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/), in branch 1 of the [unitary hypotheses](/proof/unitary-hypotheses/) below the step [HypsAlt is nonempty](/step/nonempty-hyps/).

**Setting.** Let $D$ be a datum with a chain of length $m$, block size $t$ and first rank $r$, as in [theta towers](/learn/theta/#theta-towers). Let $A$ be a family of characters indexed by a type $T$, let $R$ be a real realisation of $A$ over a number field, and let $F$ be a face. For each row $\tau \in T$, the realisation gives a [theta chain](/learn/theta/#the-global-theta-lift) with stages $Y_0, \dots, Y_{m-1}$ and a last space $H_\tau$, a set $S_\tau$ of bad places, and maps $\iota_k$ from the forms of $Y_{k+1}$ to the forms of $Y_k$. For an eigensystem $c$, the *row part* $W(\tau, c)$ is a space of forms on $Y_0$.

**Definition 2.6.1 (Up images and reached forms).** A form $x$ of $Y_{k+1}$ is an *up image* of a form $u$ of $Y_k$ if $\langle x, y \rangle_{k+1} = \langle u, \iota_k y \rangle_k$ for every form $y$ of $Y_{k+1}$. So the up map is the adjoint of $\iota_k$. The same definition with $H_\tau$ in place of $Y_{k+1}$ gives the up images at the top step. The *reached forms* are $\mathcal{R}_0(\tau, c) = W(\tau, c)$ and, for $k \geq 0$, the set $\mathcal{R}_{k+1}(\tau, c)$ of up images of elements of $\mathcal{R}_k(\tau, c)$.

**Definition 2.6.2 (Scalar law).** The realisation $R$ satisfies the *scalar law* if there are real numbers $\kappa_j > 0$ for $1 \leq j \leq m$ such that for each $\tau$ and each eigensystem $c$ with $W(\tau, c) \neq 0$, the eigensystem $c$ has a parameter system $B$ off $S_\tau$, and for each such $B$:

1. for each $k$ with $k + 1 < m$ there is a value $l$ of the partial $L$-function of $B$ at the index $k+1$ such that each $u \in \mathcal{R}_k$ has an up image, and for up images $x_1, x_2$ of $u_1, u_2 \in \mathcal{R}_k$,
$$\langle x_1, x_2 \rangle_{k+1} = \kappa_{k+1}\, l\, \langle u_1, u_2 \rangle_k;$$
2. the same holds at the top step, from $Y_{m-1}$ to $H_\tau$, with $\kappa_m$ and the value at the index $m$.

The law gives the step constant as $\kappa_{k+1} l$. Since $\kappa_{k+1} > 0$, the sign and the vanishing of the step constant are those of the $L$-value.

The main analytic input is the Rallis inner product formula, for theta lifts $\theta(\Phi, u)$ between hermitian spaces $A$ and $B$. In it, $S$ is a finite set of finite places, $\mathrm{Off}$ is the set of elements of $U(A)(\mathbb{A})$ that are integral off $S$, and $d^S$ is the product of normalising zeta factors off $S$.

**Theorem 2.6.3 (Rallis inner product formula).** Let $(A, B)$ be a pair of hermitian spaces for the [doubling method](/learn/theta/#the-doubling-method), with Weil representation $\omega$, such that $B$ has rank $\dim A + t$ with $t \geq 2$, and the Witt index of $B$ is $0$ or less than $t$. Let $S$ be a finite set of places, $\Phi_1, \Phi_2$ Fock vectors that are unramified off $S$, and $u_1, u_2$ cusp forms on $U(A)$, where $u_1$ has Hecke parameters off $S$ and $u_2$ is spherical off $S$. Assume that at some split place outside $S$ the parameters satisfy the nonvanishing condition, and that the doubling integrand is integrable on $\mathrm{Off}$ at some $s_1 < t/2$. Then the lifts converge, $g \mapsto \langle \omega(g)\Phi_1, \Phi_2 \rangle \langle \pi(g) u_1, u_2 \rangle$ is integrable on $\mathrm{Off}$, and for every value $l$ of $L^S(s + \tfrac12)$ at $s = t/2$,
$$\langle \theta(\Phi_1, u_1), \theta(\Phi_2, u_2) \rangle = \mathrm{vol}(B) \cdot \frac{l}{d^S(t/2)} \int_{\mathrm{Off}} \langle \omega(g)\Phi_1, \Phi_2 \rangle\, \langle \pi(g) u_1, u_2 \rangle\, dg.$$
(W. T. Gan, Y. Qiu and S. Takeda, *The regularized Siegel-Weil formula (second term identity) and the Rallis inner product formula*, Invent. Math. 198 (2014).) We use it as a hypothesis.

**Theorem 2.6.4 (Step scalars).** Assume the following published results: the finiteness theorem of Harish-Chandra, the rapid decay of cusp forms, the cover by discrete series, the theory of Harish-Chandra modules, the Casselman-Wallach theorem, the unramified Howe correspondence and the unramified doubling identity. Assume that $R$ and $F$ satisfy the standing conditions below, that $D$ satisfies the node gap condition, and that the Rallis inner product formula holds for $D$. Then $R$ satisfies the scalar law.

Lean: `GlobalTheory.ChainTw.scalars_of_given_all` (also `GlobalTheory.T.thetaChain_steps_positive_multiple_of_LValue`, a second name).

The *standing conditions* on $R$ and $F$ are: a core condition; the existence of size data with a parameter choice; the absolute irreducibility of the characters of $A$; good types at the places of the group; a guard condition; and the gaps $\lambda_n - \lambda_{n+1} \geq 100 r^4$ between consecutive highest weight entries, for $n + 1 < r$. The *node gap condition* says that consecutive nodes of the highest weight data are far apart, compared to $t$ and the rank.

*Proof.* The proof has two halves: facts about a step of the twisted chain of $D$, and facts about the realisation $R$.

1. *Facts at the stages.* Each stage has finite dimensional spaces of forms with inner products; this uses the finiteness theorem of Harish-Chandra and the rapid decay. The twisted chain satisfies its level laws, its Euler factors at the twist places can be restored, and the partial $L$-function of the chain factors through the quotients of the stages. The lifts span the next stage (from the discrete series, the Harish-Chandra modules, the Casselman-Wallach theorem and the level laws), and they are adjoint to the maps $\iota_k$ (from the rapid decay). Together these show that the up map is the theta lift.
2. *The exact inner product.* At each step, for forms $u_1, u_2$ of the stage, where $u_1$ has Hecke parameters $B$ and the twisted type of the chain, and for every value $l$ of the partial $L$-function at $t/2$,
$$\langle \theta(u_1), \theta(u_2) \rangle = \overline{\mathrm{vol} \cdot \frac{l}{d^S} \cdot \prod_{\mathfrak{P} \in Q} \ell_{\mathfrak{P}} \cdot Z_\infty} \cdot \langle u_1, u_2 \rangle,$$
where $Z_\infty$ is a real zeta integral over the level set. This comes from the Rallis inner product formula. [The peeling of the twist places](/entry/q-peel-holds/) replaces the integral over $\mathrm{Off}$ by the integral over the level set times the product of the local factors, and the twisted transform laws turn the integral over the level set into the real zeta integral.
3. *The step constant.* The exact inner product gives the step constant in the form $\kappa \cdot l$ with $\kappa \neq 0$. To apply step 2 at every stage, the forms reached at the index $k$ must have known Hecke parameters and the twisted type of the chain. The parameters come from the unramified Howe correspondence. The twisted type comes from [the Hecke parameters along the chain](/entry/up-q-holds/), started at the index $0$ by a lemma that gives the lower block parameter at the first stage.
4. *Facts about the realisation.* From the standing conditions: the top step has the expected range; each row $\tau$ gives a twisted chain of $D$ whose stages are those of the realisation; the real zeta integrals do not vanish (from the archimedean theta correspondence); and the step constants do not depend on the row. The last fact uses the node gap condition, the restored Euler factors, the uniformity of the measures, the growth of the quotient volumes and a bound for the norms of the data.
5. *Assembly.* A last lemma puts together steps 3 and 4, the lower block parameter, the positivity of the $L$-values at the first stage, the normalisation of the last stage, the parameters of the rows and the agreement of the types. It gives the scalar law. $\square$

**Theorem 2.6.5 (Step scalars under the standing hypotheses).** Assume the seven published results of the last theorem, and assume that the Rallis inner product formula holds for every datum. If $R$ and $F$ satisfy the standing conditions, then $R$ satisfies the scalar law.

Lean: `GlobalTheory.Core.Rk.ScalarsRow.scalars_of_heckeFormNS`.

*Proof.* The parameter choice in the standing conditions has a node gap that is at least cubic in the rank. A lemma on the nodes of Harish-Chandra parameters turns this into the node gap condition for $D$. Now apply the theorem on step scalars, with the Rallis inner product formula at $D$. $\square$

**Theorem 2.6.6 (Step scalars, full list of hypotheses).** Assume the seven published results, the Weil-Siegel formula for unitary groups, the Rallis inner product formula for every datum and the meromorphic continuation of Siegel Eisenstein series. If $R$ and $F$ satisfy the standing conditions and the ideal $\mathfrak{c}_K$ of the host of $D$ is the unit ideal, then $R$ satisfies the scalar law.

Lean: `GlobalTheory.Core.Rk.ScalarsRow.scalars` (also `GlobalTheory.T.thetaChainStep_positive_scalar_standingHypotheses`, a second name).

*Proof.* This is the last theorem; the Weil-Siegel formula, the continuation of Eisenstein series and the condition on $\mathfrak{c}_K$ are not used. $\square$

**Remark 2.6.7 (Formalization).** The theorem on step scalars is at [ScalarsOfGivenData.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ScalarsOfGivenData.lean#L48), and the other two at [ThetaChainStepPositiveScalarStandingHypotheses.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypotheses.lean#L29) (lines 29 and 39). The scalar law is defined in [LabelSettingScalars.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/LabelSettingScalars.lean#L74), the Rallis formula in [HeckeFormNSOfHeckeForm.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/HeckeFormNSOfHeckeForm.lean#L202), the exact inner product of step 2 in [StepExactNS.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/StepExactNS.lean#L89), and the standing conditions in [RealLowestKTypeCoeffSquareIntegrable.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L28). The proof of the main theorem is a list of about twenty lemmas, one or two for each step; we have read the lines that apply them, not their proofs, and steps 1 to 5 describe them by their statements and names. We have not unfolded the partial $L$-function, the parameter systems, the value predicate for $L$, the core and guard conditions, the good types, the Fock vectors and the nonvanishing condition at a split place. The middle theorem asks for the Rallis formula at every datum but uses it only at $D$, and it does not use the size data that it obtains from the parameter choice. The last theorem does not use three of its hypotheses, and the lemma on the lower block parameter at the first stage is applied twice in the main proof (lines 60 and 66).

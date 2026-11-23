---
id: scalar-step
title: An almost cocycle with an A_inf coboundary is near a crystalline cocycle
kind: theorem
decl: GlobalTheory.Cyc.ClassBound.scalar_step
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineExtensionClassBound
covers: 372
status: drafted
drafted_by: writer@claude
---
This lemma is the analytic core of [the class bound](/entry/class-bound/). A function $c \colon G_{K_s} \to \mathbb{Q}_\ell$ that is a cocycle for $\mathbb{Q}_\ell(-e)$ up to $\mathbb{Z}_\ell$, and whose multiple $\ell^N c$ is a coboundary in $B_{\mathrm{dR}}$ up to $A_{\inf}$ and $\mathrm{Fil}^{e+1}$, is close to a true crystalline cocycle after one more explicit power of $\ell$. It is used once, in [the scalar lemma](/entry/scalar-of-is-cob/). It chains three lemmas, each with its own loss of powers of $\ell$.

## Statement

Let $\ell$ be prime, $K$ a finite extension of $\mathbb{Q}_\ell$, $s \geq 1$ with $s \geq 2$ if $\ell = 2$, and $K_s = K_0(\mu_{\ell^s})$ as in [the class bound](/entry/class-bound/). Let $\chi$ be the cyclotomic character, $B \subset B_{\mathrm{dR}}$ the period rings of $D$ at $\ell$ with the filtration $\mathrm{Fil}^\bullet$, and $\iota \colon A_{\inf} \to B_{\mathrm{dR}}$. Assume local Tate duality and Tate's Euler characteristic formula. Let $e, r, N \geq 0$ and $c \colon G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$. Suppose that for $\sigma, \tau \in G_{K_s}$:

1. $|c(\sigma)| \leq \ell^r$;
2. $|c(\sigma\tau) - c(\sigma) - \chi(\sigma)^{-e} c(\tau)| \leq 1$;
3. $|c(\tau) - c(\sigma)| \leq 1$ for $\tau$ near $\sigma$;
4. there is $b \in \mathrm{Fil}^0$ such that for each $\sigma$ there is $a \in A_{\inf}$ with $\ell^N c(\sigma) - (\chi(\sigma)^{-e}\sigma(b) - b) - \iota(a) \in \mathrm{Fil}^{e+1}$.

Then there are $z \colon G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$ and $x \in B$ such that $z$ is a continuous cocycle on $G_{K_s}$ for $\chi^{-e}$, $z(\sigma) = \chi(\sigma)^{-e}\sigma(x) - x$ for $\sigma \in G_{K_s}$, and
$$|z(\sigma) - \ell^{k} c(\sigma)| \leq 1, \qquad k = N + a_e + m_e, \quad m_e = s + v_\ell(e+1), \quad a_e = (e+2)s + v_\ell(e) + \lfloor e/(\ell-1) \rfloor + 1.$$

So $z$ is a crystalline class in $H^1(K_s, \mathbb{Q}_\ell(-e))$, and it agrees with $\ell^k c$ modulo $\mathbb{Z}_\ell$.

## Proof

1. **Lift.** `TwistLift.lift_cocycle` gives a true continuous cocycle $z_0$ with $|z_0 - \ell^{m_e} c| \leq 1$. It uses local Tate duality.
2. **Transport of condition 4.** Write $z_0(\sigma) = u + \ell^{m_e} c(\sigma)$ with $u \in \mathbb{Z}_\ell$. Then $\ell^N z_0$ satisfies condition 4 with $b' = \ell^{m_e} b$ and $a' = \ell^{m_e} a + \ell^N u$. To see that $\iota(u) = u$, the proof uses `padicInt_hom_witt_ext_pt`: two ring maps $\mathbb{Z}_\ell \to W(R)$ agree when $R$ has characteristic $\ell$.
3. **Dual exponential.** `ExpScalar.exists_expStar_zero_near` gives a cocycle $z$ with $|z - \ell^{a_e} \ell^N z_0| \leq 1$ that satisfies `ExpStar` with $\alpha = 0$: $z(\sigma) - (\chi(\sigma)^{-e}\sigma(b'') - b'') \in \mathrm{Fil}^{e+1}$ for some $b'' \in \mathrm{Fil}^0$. The Lean names read this as "the dual exponential of $z$ is zero".
4. **Crystalline.** `coboundary_bcris_of_dualExponential_zero` gives $x \in B$ with $z(\sigma) = \chi(\sigma)^{-e}\sigma(x) - x$.

The bound follows from the ultrametric inequality:
$$z - \ell^{k} c = \bigl(z - \ell^{a_e}\ell^N z_0\bigr) + \ell^{a_e + N}\bigl(z_0 - \ell^{m_e} c\bigr).$$

## In the Lean code

The lemma is at [CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L140). The lemmas it calls:

- `GlobalTheory.Cyc.TwistLift.lift_cocycle`, in [ContinuousFixingSubgroupEquiv.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ContinuousFixingSubgroupEquiv.lean#L384);
- `GlobalTheory.Cyc.ExpScalar.exists_expStar_zero_near`, in ExistsExpStarZeroNear.lean;
- `GlobalTheory.T.coboundary_bcris_of_dualExponential_zero`, a second name for `KerExpCrys.cob_cris_of_expStar_zero`;
- `padicInt_hom_witt_ext_pt`, in the same file.

We read the statements of the three named lemmas, not their proofs. `ExpStar` is in [ExpStar.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExpStar.lean#L40). `lift_cocycle` takes the Euler characteristic formula but drops it: its proof starts `fun D h2 _ l ...`. Condition 1 is also dropped there. The filtration is that of the period data at $\mathbb{Q}_\ell$ (`botExt l`); it is the same for every $K$ by the field `PD_Fil`.

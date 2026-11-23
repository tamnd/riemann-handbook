---
id: transported-fund-domain-volume-classical
title: The volume of the transported fundamental domain, statement form
kind: theorem
decl: GlobalTheory.T.transportedFundDomain_volume_classical
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TransportedFundDomainVolumeClassicalStatement
covers: 546
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`CovDom.main`](/entry/cov-dom-main/). Its only user is [`CovNFormulaPf.main`](/entry/cov-nformula-pf-main/). The content is in [`CovDom.main`](/entry/cov-dom-main/) and in the volume formula [`covolume_N`](/entry/covolume-n/) below it.

## Statement

Use the notation of [the parent entry](/entry/cov-nformula-pf-main/): $r$, $k$, $f$ and the root discriminant $2v$ of $E$.

**Theorem.** For every setting $X$, every `Full` record $Y$, every real $\theta$, every choice $C$ and every word $u$, the image of the fundamental domain $F_N(u)$ under the transport map has measure
$$(2v)^{(r^2 + rk + r/2)\,f}$$
for the product of $f$ copies of the Lie algebra Haar measure with scale 1 on the model unipotent group $N$.

The transport map sends a point $x$ of the real group to the family $\tau \mapsto Q'_\tau\, x_\tau\, Q_\tau$. Here $x_\tau$ is the matrix of $x$ at the place of $\tau$, and $Q_\tau$ and $Q'_\tau$ are the fields `C.Q` and `C.Qi` of the choice. The statement takes the measure with `toReal`.

## Proof

The proof is the term `GlobalTheory.CovDom.main`. There is nothing else.

## In the Lean code

The theorem is at [TransportedFundDomainVolumeClassicalStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TransportedFundDomainVolumeClassicalStatement.lean#L10). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The right side does not depend on $\theta$, $C$ or $u$. The word "classical" in the name is only a label.

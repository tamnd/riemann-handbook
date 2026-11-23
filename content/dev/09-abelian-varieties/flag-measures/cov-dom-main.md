---
id: cov-dom-main
title: The volume of the transported fundamental domain
kind: theorem
decl: GlobalTheory.CovDom.main
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TransportedFundDomainVolumeClassical
covers: 545
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement of [`transportedFundDomain_volume_classical`](/entry/transported-fund-domain-volume-classical/). That statement feeds the closed formula [`CovNFormulaPf.main`](/entry/cov-nformula-pf-main/) for the step [nonempty hypotheses](/step/nonempty-hyps/). The proof puts the concrete data of the global datum into the abstract volume formula [`covolume_N`](/entry/covolume-n/), and then evaluates the constant.

## Statement

The statement is the one in [the parent entry](/entry/transported-fund-domain-volume-classical/). The image of the fundamental domain $F_N(u)$ under the transport map has measure $(2v)^{(r^2 + rk + r/2) f}$.

## Proof

1. **The data.** The file `Direct.lean` defines the Gram matrix $J$, the lattice $\Lambda$, the frame $P$ of the word $u$, the dual tuple $f$, the integer $T$, the model matrices $A_w$ and the scales $s_a = (2v)^{r-a}$.
2. **The hypotheses of `covolume_N`.** These results give them:
   - `isCMExt_host` and the local lemma `formallyUnramified_host` give the CM and unramified conditions on $E/F$;
   - `concrete_gram_hermitian_nondegenerate_lattice_selfDual` says that $J$ is Hermitian and nondegenerate and that $\Lambda$ is self-dual;
   - `wordFrame_dualTuple_gram_integrality` gives the frame, the dual tuple and the lattice inclusion;
   - `bessel_transport_isometry_frame_adapted` says that each $A_w$ takes $w(J)$ to the model form and is adapted to $P$, $f$ and $s$;
   - `fundamental_domain_normalising_constants` gives $s_a > 0$.
3. **The domain.** The local lemma `isDomN` shows that the transported domain, read at the infinite places of $E$, is a domain in the sense of `covolume_N`. Every point of the product of the model groups is a translate of exactly one point of the domain. The proof uses the strict fundamental domain property of $F_N(u)$. It also uses the facts that the transport map is a bijective homomorphism, and that the integral unipotent group is the same as the lattice stabilizer in coordinates. The lemma `cancel_conj` removes the conjugation by $A_w$.
4. **The volume.** `covolume_N` gives the measure as $|d_F|^{e}\,(\prod_a s_a^{4(r-a)+2k})^{f}$ with $e = -(k+1)r^2 - 4(r^3 - r)/3 - 3r/2$. The second part of `fundamental_domain_normalising_constants` says that this number is $(2v)^{(r^2+rk+r/2)f}$.
5. **Reindexing.** `measurePi_pointsAtInfinitePlacesCMType_image` says that the product measure over `Tau` equals the product measure over the infinite places of $E$ after the reindexing map.

## In the Lean code

The theorem is at [TransportedFundDomainVolumeClassical.lean line 89](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TransportedFundDomainVolumeClassical.lean#L89). The lemma `isDomN` is at [line 45](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TransportedFundDomainVolumeClassical.lean#L45). The data start at [Direct.lean line 31](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/Direct.lean#L31). The reindexing map `Gm` sends a family over `Tau` to a family over the places $w$. At a place whose embedding is not the embedding attached to its element of `Tau`, it conjugates the entries. The matrices $A_w$ are conjugated in the same way. This entry does not unfold the arithmetic in `fundamental_domain_normalising_constants`. A hand check with $|d_F| = (2v)^f$ gives the same exponent.

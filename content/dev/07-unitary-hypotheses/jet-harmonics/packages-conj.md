---
id: packages-conj
title: The two packages at a prime where Frobenius is complex conjugation
kind: theorem
decl: GlobalTheory.PkgConj.packages_conj
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.PackagesExistFrobeniusComplexConjugation
covers: 318
status: drafted
drafted_by: writer@claude
---
This theorem proves the two package statements `PkgPhiCSt` and `PkgZeroCSt` from the chart statement `UpFSt`. Its alias [`packages_exist_frobeniusComplexConjugation`](/entry/packages-exist-frobenius-complex-conjugation/) gives them to [`goodPrime_packages`](/entry/good-prime-packages/). The row family and the bound on $\nu$ come from [`exists_rowFam`](/entry/exists-row-fam/). This theorem fills the other fields, which is arithmetic.

## Statement

Use the setting of `AllPts` in [the entry for `goodPrime_packages`](/entry/good-prime-packages/): a numerical datum $N$ with ranks $k, m$, $r = k + m - 1$ and $f$ places $z$, an index $1 \le j \le m$, an injective map $p_l$ from the places to the embeddings $E \to \mathbb{C}$, a dominant weight $a$, a prime $\lambda$ of residue characteristic $\ell$ with `PhiC N ℓ`, and $n_W$, $\nu$. Let $P$ = `parOf N j ℓ`. For an embedding $\tau$ let $\mathrm{mult}(\tau)$ be $p$ if $\tau$ is in the image of $p_l$ and $q$ if not, where $(p,q) = (k+j-1, m-j)$ is the signature. Let $\tau(z,0) = p_l(z)$, $\tau(z,1) = \overline{p_l(z)}$, and

$$g(z,s,i) = \mathrm{gap}\bigl(\mathrm{mult}\,\tau(z,s),\ a(\tau(z,s), \cdot)\bigr)(i),$$

where $\mathrm{gap}(r,b)(i) = b(i-1) - b(i)$ for $1 \le i \le r$, with $b(r)$ read as $0$, and $0$ for other $i$.

**Theorem.** Assume `UpFSt p` for all primes $p$. Then, in the setting of `AllPts`:

1. (`PkgPhiCSt`) For all reals $T, \theta_0, C_1$ with `DegHyp2` for $P$, the weight $W(z) = a(p_l z, k-2) - a(p_l z, k-1)$ and the rest `restOf`, and with $8rf \le n_W$, there is a package `PkgPhiC` $P$ $\ell$ $C_1$ whose fields $T$ and $\nu$ are the given ones.
2. (`PkgZeroCSt`) If the weights $w_j$ of $N$ are nonnegative, $a(\tau, 0) \le s(\ell - 1)$ for each $\tau$ with $\mathrm{mult}(\tau) > 0$, and $4rsf \le n_W$, then there is a package `PkgZeroC` $P$ $\ell$ whose field $\nu$ is $\nu$.

Each package is a row family $R$ with weights $g$, the given numbers, and the block bound `ValBlocksC` on $\nu$. `PkgPhiC` also asks that the rows be alternating, that $g(z,0,k-1) = W(z)$, and that its rest be $\sum_{z,s} \sum_{i \le r} i\, g(z,s,i)$ without these main terms. `PkgZeroC` asks $\sum_{i \le K} g(z,\sigma,i) \le s(\ell-1)$ for some $K$ with $4Ksf \le n_W$.

## Proof

Both parts call [`exists_rowFam`](/entry/exists-row-fam/). It gives a bijection $(z,s) \mapsto \tau(z,s)$ onto the embeddings, and a row family $R$ with alternating rows, ranks $\operatorname{rk} R_z(0,s) = \mathrm{mult}\,\tau(z,s)$, and `ValBlocksC`.

1. By `gap_sums` the weights $g$ are supported in $[1, \mathrm{mult}]$. As $\mathrm{mult}\, p_l(z) = k+j-1 \ge k-1$, the weight $g(z,0,k-1)$ is $W(z)$. Then `gap_sums` gives $\sum_i i\, g(z,s,i) = \sum_{i < \mathrm{mult}} a(\tau(z,s), i)$. The bijection turns the sum over $(z,s)$ into $\mathrm{DF} = \sum_\tau \sum_{i < \mathrm{mult}\,\tau} a(\tau,i)$, so the rest is $\mathrm{DF} - (k-1)\sum_z W(z)$, which is `restOf`. The private lemma `rest_add` does the subtraction. The other hypotheses go in unchanged.
2. Take $K = r$ and $T = 1$. By `gap_sums` the sum $\sum_{i \le r} g(z,\sigma,i)$ telescopes to $a(\tau(z,\sigma), 0)$, or to $0$ when the multiplicity is $0$.

## In the Lean code

The theorem is in [PackagesExistFrobeniusComplexConjugation.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PackagesExistFrobeniusComplexConjugation.lean#L84). The weights $g$ are `gaC` (line 21). It calls:

- `GlobalTheory.PkgConj.exists_rowFam`, in the same file;
- `gap_sums` in [GapParts.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/GapParts.lean#L45), and `rest_add` in the same file.

`PkgPhiC`, `PkgZeroC` and `DegHyp2` are in [RestNonneg.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RestNonneg.lean#L76). `UpFSt` is used only to call `exists_rowFam`. The hypotheses $\ell \ne q_N$, $\ell \ne d_N$ and ($\ell$ inert $\Rightarrow 5 \le \ell$) are passed to `exists_rowFam`, which does not use them.
